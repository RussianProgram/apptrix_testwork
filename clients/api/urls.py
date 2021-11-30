from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('clients/',
         views.ClientListView.as_view(),
         name='client_list'),
    path('clients/<pk>',
         views.ClientDetailView.as_view(),
         name='client_detail'),

]