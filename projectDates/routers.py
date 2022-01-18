from rest_framework.routers import DefaultRouter
from django.urls import path,include
from clients.api.views import ClientViewSet

router = DefaultRouter()
router.register(r'clients',ClientViewSet,basename='client')
urlpatterns = [
    path('',include(router.urls))
]