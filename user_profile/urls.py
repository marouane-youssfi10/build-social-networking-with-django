from django.urls import path
from . import views


urlpatterns = [
    path('feed/', views.index, name="index"),
    path('<slug:name_user>/<int:pk>/', views.user_profile, name="user-profile"),

    path('accounts-setting/edit-profile/', views.edit_profile, name="edit-profile"),

    path('accounts-setting/edit-profile/update-experience/<int:pk>/', views.edit_experience_user, name="edit-user-experience"),
    path('accounts-setting/edit-profile/create-experience/', views.create_experience_user, name="create-user-experience"),
    path('accounts-setting/edit-profile/delete-experience/<int:pk>/', views.delete_experience_user, name="delete-user-experience"),

    path('accounts-setting/edit-profile/create-link-media/', views.create_links_media, name="create-links-media"),
    path('accounts-setting/edit-profile/update-link/<int:pk>/', views.edit_links_media, name="edit-links-media"),
    path('accounts-setting/edit-profile/delete-link/<int:pk>/', views.delete_links_media, name="delete-links-media"),

    path('accounts-setting/edit-profile/?delete-tag=<int:pk>/', views.delete_tags_user, name="delete-user-tags"),
    path('accounts-setting/edit-profile/create-tags/', views.create_tags_user, name="create-user-tags"),

    path('saved-jobs/<int:pk>', views.saved_jobs, name='saved-jobs'),
    path('unsaved-jobs/<int:pk>', views.unsaved_jobs, name='unsaved-jobs'),

    path('bid-project/<int:pk>', views.bid_project, name='bid-project'),
    path('unbid-project/<int:pk>', views.unbid_project, name='unbid-project'),
]
