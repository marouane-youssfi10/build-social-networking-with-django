from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.inbox, name="messages"),
    path('messages/<int:message_user_id>', views.conversations, name="conversation"),
    path('send/<int:the_user_id>/', views.send_message, name="send")
]