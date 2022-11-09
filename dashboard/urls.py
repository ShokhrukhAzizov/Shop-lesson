from django.urls import path
from .views import dashborad_view

urlpatterns = [
    path('', dashborad_view, name='dashboard_url'),
]