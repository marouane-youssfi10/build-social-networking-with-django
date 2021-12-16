from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.inbox, name="messages"),
    path('messages/<str:message_user>/<int:message_user_id>/', views.conversations, name="conversation"),
    path('send-messages/send/<int:to_user>/', views.send_message, name="send-message"),
    path('<int:pk>/', views.add_user_to_conversation, name="add-user-to-conversation")
]