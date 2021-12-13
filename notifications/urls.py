from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.show_notifications, name="show-notifications")
]