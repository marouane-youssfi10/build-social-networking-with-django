from django.urls import path
from . import views

urlpatterns = [
    path('show-notifications/', views.Show_notifications, name="show-notifications")
]