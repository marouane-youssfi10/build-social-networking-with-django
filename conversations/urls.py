from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.inbox, name="messages"),
    path('messages/', views.inbox, name="conversations"),
]