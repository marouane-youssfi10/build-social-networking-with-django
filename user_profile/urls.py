from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user-profile', views.user_profile, name="user-profile"),
]