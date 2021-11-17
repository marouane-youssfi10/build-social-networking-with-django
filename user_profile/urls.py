from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user-profile/', views.user_profile, name="user-profile"),

    path('accounts-setting/change-password/', views.change_password, name="change-password"),
    path('accounts-setting/edit-profile/', views.edit_profile, name="edit-profile"),
    path('accounts-setting/edit-profile/edit_experience/', views.edit_experience_user, name="edit-user-experience"),
    path('accounts-setting/edit-profile/delete_tags/', views.delete_tags_user, name="delete-user-tags"),

    path('accounts-setting/edit-profile/create_tags/', views.create_tags_user, name="create-user-tags"),
]