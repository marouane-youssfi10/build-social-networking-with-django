from django.urls import path
from . import views

urlpatterns = [
    path('', views.Show_notifications, name="show-notifications")
]