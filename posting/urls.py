from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.index, name="projects"),
    path('post-project/', views.post_projects, name="post-project"),
    path('jobs/', views.post_job, name="post-job"),
    path('search/', views.post_job, name="search"),
]