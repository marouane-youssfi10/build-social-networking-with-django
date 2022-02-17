from django.urls import path, include
from .views import RegistrationNewUserAPI, MyTokenObtainPairView
from .rest_views.posting_views import PostingProjectAPIView, PostingJobAPIView ,PostingProjectViewsets, PostingJobViewsets
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects', PostingProjectViewsets, basename='projects')
router.register('jobs', PostingJobViewsets, basename='jobs')

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegistrationNewUserAPI.as_view(), name='register_new_user'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),

    path('posting-project/', PostingProjectAPIView.as_view(), name='posting'),
    path('posting-job/', PostingJobAPIView.as_view(), name='job'),


]