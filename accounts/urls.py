from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"), # http://127.0.0.1:8000/login/
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register")
]