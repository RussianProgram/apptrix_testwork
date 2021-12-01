from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,GenericAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from ..models import Client,Liked
from ..tasks import match_created

from .serializers import ClientSerializer,UserSerializer

from django.contrib.auth.models import User
from django_filters import rest_framework as filters



class ClientsListFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name='user__first_name')
    last_name = filters.CharFilter(field_name='user__last_name')
    class Meta:
        model = Client
        fields = ['sex']

class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClientsListFilter

class ClientDetailView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

class ClientMatchView(GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)

        liked_from = Liked.objects.filter(like_from=user, like_to=request.user)
        liked_to = Liked.objects.filter(like_from=request.user, like_to=user)

        if user != request.user:
            if liked_from:
                if liked_to:
                    return Response({'Status': 'your already inlove'})
                Liked.objects.create(like_from=request.user, like_to=user)
                match_created.delay(request.user.username,
                                    request.user.email,
                                    user.email)
                match_created.delay(user.username,
                                    user.email,
                                    request.user.email)
                return Response({'Good':f'Now check your mail'})

            else:
                Liked.objects.create(like_from=request.user,like_to=user)
                return Response({'Half good':'its his time'})
        else:
            return Response({'Static':'You cant be inlove in yourself'})