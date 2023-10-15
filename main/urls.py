from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import ClientCreateView, ClientUpdateView, ClientDeleteView, ClientListView, HomeView

urlpatterns = [
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('', cache_page(60)(HomeView.as_view()), name='home'),
]