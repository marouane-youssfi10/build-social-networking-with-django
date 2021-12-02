from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:pk>', views.follow_profile, name="follow"),
    path('unfollow/<int:pk>', views.unfollow_profile, name="unfollow"),
    path('add-like/<int:pk>', views.add_like, name="add-like"),
    path('remove-like/<int:pk>', views.remove_like, name="remove-like"),

]