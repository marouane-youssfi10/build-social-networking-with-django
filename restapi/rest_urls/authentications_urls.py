from django.urls import path, include
from restapi.views import RegistrationNewUserAPI, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegistrationNewUserAPI.as_view(), name='register_new_user'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
]