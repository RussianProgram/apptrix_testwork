import django_filters
from rest_framework.filters import BaseFilterBackend
from geopy.distance import great_circle
from django_filters import rest_framework as filters
from .models import Client

"""
Кастомный фильтр для вычисления дистанции
    между участниками и фильтрации их по значению в метрах.
"""
class DistanceFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        qp = request.query_params.get('distance')
        if qp:
            user_location = (
                float(request.user.client.longitude),
                float(request.user.client.latitude)
            )
            distance_filter = float(qp)

            new_qs = set()
            for client in queryset:
                if client.user != request.user:
                    client_location = (
                        client.longitude,
                        client.latitude
                    )
                    distance_between = great_circle(user_location,client_location).meters
                    if distance_between < distance_filter:
                        new_qs.add(client.pk)

            return queryset.filter(pk__in=new_qs)
        else:
            return queryset

"""
Фильтрация по Имени,Фамилии и полу
"""
class BaseClientFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name='user__first_name')
    last_name = filters.CharFilter(field_name='user__last_name')
    class Meta:
        model = Client
        fields = ['sex']


