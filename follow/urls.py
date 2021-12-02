from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:pk>', views.follow_unfollow_profile, name="follow"),
]