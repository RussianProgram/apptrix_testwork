from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from ..models import Client
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