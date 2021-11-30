from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from ..models import Client
from .serializers import ClientSerializer
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