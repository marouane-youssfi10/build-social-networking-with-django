from django.urls import path, include
from rest_framework import routers
from restapi.rest_views.conversation_views import ConversationAPIView, ConversationViewsets

router = routers.DefaultRouter()

# conversation section
router.register('conversations', ConversationViewsets, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
    path('get-user-conversations/', ConversationAPIView.as_view(), name='user-conversation'),

]