from django.urls import path, include
from rest_framework import routers
from restapi.rest_views.follow_views import FollowViewsets, FollowAPIView, get_user_follow

router = routers.DefaultRouter()

# follow section
router.register('follow', FollowViewsets, basename='follow')

urlpatterns = [
    path('', include(router.urls)),

    path('get-user-follow/', FollowAPIView.as_view(), name='user-follow'),
    path('get-user-follow/<int:pk>/', get_user_follow, name='get-user-follow')

]