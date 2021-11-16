from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user-profile/', views.user_profile, name="user-profile"),
    path('accounts-setting/change-password/', views.change_password, name="change-password"),
    path('accounts-setting/edit-profile/<int:pk>/', views.edit_profile, name="edit-profile")
]