from django.urls import path, include
from rest_framework import routers
from restapi.rest_views.notifications_views import NotificationsViewsets, NotificationsAPIView

router = routers.DefaultRouter()

# notifications section
router.register('notification', NotificationsViewsets, basename='update-notification-seen')

urlpatterns = [
    path('', include(router.urls)),
    path('get-notifications/', NotificationsAPIView.as_view(), name='notifications'),
]