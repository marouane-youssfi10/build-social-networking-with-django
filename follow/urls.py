from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:pk>', views.follow_profile, name="follow"),
    path('unfollow/<int:pk>', views.unfollow_profile, name="unfollow"),

    # for projects posts this likes
    path('add-like/<int:pk>', views.add_like_projects, name="add-like-post-projects"),
    path('remove-like/<int:pk>', views.remove_like_projects, name="remove-like-post-projects"),

    # for jobs posts this likes
    path('add-like/<int:pk>', views.add_like_jobs, name="add-like-post-jobs"),
    path('remove-like/<int:pk>', views.remove_like_jobs, name="remove-like-post-jobs"),

]