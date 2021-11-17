from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user-profile/', views.user_profile, name="user-profile"),

    path('accounts-setting/change-password/', views.change_password, name="change-password"),
    path('accounts-setting/edit-profile/', views.edit_profile, name="edit-profile"),
    path('accounts-setting/edit-profile/experience/', views.edit_experience_user, name="edit-user-experience"),
    path('accounts-setting/edit-profile/tags/', views.edit_tags_user, name="edit-user-tags")
]