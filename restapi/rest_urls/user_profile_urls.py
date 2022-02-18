from django.urls import path, include
from rest_framework import routers

from restapi.rest_views.user_profile_views import UserProfileAPIView, UserProfileViewsets


router = routers.DefaultRouter()

#
router.register('user-profile', UserProfileViewsets, basename='user-profile')

urlpatterns = [
    path('', include(router.urls)),

    path('my-profile/', UserProfileAPIView.as_view(), name='my-profile'),


]