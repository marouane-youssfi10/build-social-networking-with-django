from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.inbox, name="messages"),
    path('messages/<str:message_user_id>', views.conversations, name="conversation"),
]