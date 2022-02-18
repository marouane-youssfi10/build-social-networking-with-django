from django.urls import path, include
from .views import RegistrationNewUserAPI, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from .rest_views.posting_views import (
    PostingProjectAPIView,
    PostingJobAPIView,
    PostingProjectViewsets,
    PostingJobViewsets,

    DeleteTagsProjectsViewsets,
    DeleteTagsJobsViewsets
)
from .rest_views.follow_views import FollowViewsets, FollowAPIView
from .rest_views.follow_views import get_user_follow

router = routers.DefaultRouter()

# post project or job section
router.register('projects', PostingProjectViewsets, basename='projects')
router.register('jobs', PostingJobViewsets, basename='jobs')

# follow section
router.register('follow', FollowViewsets, basename='follow')

# delete post section
router.register('delete-tags-project', DeleteTagsProjectsViewsets, basename='delete-tags-project')
router.register('delete-tags-job', DeleteTagsJobsViewsets, basename='delete-tags-jobs')

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegistrationNewUserAPI.as_view(), name='register_new_user'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),

    path('posting-user-projects/', PostingProjectAPIView.as_view(), name='user-projects'),
    path('posting-user-jobs/', PostingJobAPIView.as_view(), name='user-jobs'),

    path('get-user-follow/', FollowAPIView.as_view(), name='user-follow'),
    path('get-user-follow/<int:pk>/', get_user_follow, name='get-user-follow')



]