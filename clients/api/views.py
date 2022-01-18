from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (AllowAny,IsAuthenticated,
                                        IsAdminUser)
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Client,Liked
from ..tasks import match_created
from ..filters import DistanceFilter,BaseClientFilter

from .serializers import (ClientSerializer,UserSerializer,
                          ClientUpdateSerialiser)


"""
Основной ViewSet для проекта
"""
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend,DistanceFilter]
    filterset_class = BaseClientFilter

    permission_classes_by_action = {
        'create': [AllowAny],
        'match': [IsAuthenticated],
        'update': [IsAuthenticated],
        'destroy': [IsAdminUser]
        }

    def create(self, request, *args, **kwargs):
        client_serialiser = self.get_serializer(data=request.data)
        client_serialiser.is_valid(raise_exception=True)
        data = client_serialiser.validated_data
        client_serialiser.save(**data)

        return Response(status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("POST",detail="Use PUT")

    """
    Логика для создания связи между участниками,
    при совместном интересе на почты обоих с помощью Celery
    отправляются уведомительные письма
    """
    @action(detail=True, methods=['get'])
    def match(self,request,pk=None):
        user = User.objects.get(id=pk)

        liked_from = Liked.objects.filter(
            like_from=user,
            like_to=request.user
        )
        liked_to = Liked.objects.filter(
            like_from=request.user,
            like_to=user
        )

        if user != request.user:
            if liked_from:
                if liked_to:
                    return Response({'Status': 'your already inlove in this person'})

                Liked.objects.create(
                    like_from=request.user,
                    like_to=user
                )
                match_created.delay(
                    request.user.username,
                    request.user.email,
                    user.email
                )
                match_created.delay(
                    user.username,
                    user.email,
                    request.user.email
                )
                return Response({'Good': f'Now check your mail'})

            else:
                if liked_to:
                    return Response({'Status': 'your already like this person'})

                Liked.objects.create(
                    like_from=request.user,
                    like_to=user
                    )
                return Response({'Half good': 'Now wait for reply'})
        else:
            return Response({'Status': 'You cant be inlove in yourself'})

    """Получить разрешение исходя из определенного вида запроса"""
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializer
        if self.action == 'update':
            return ClientUpdateSerialiser
        return ClientSerializer

