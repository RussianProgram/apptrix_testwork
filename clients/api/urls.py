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
    path('register/',
         views.CreateUserView.as_view(),
         name='user_register'),
    path('clients/<pk>/match',
         views.ClientMatchView.as_view(),
         name='client_match'),

]