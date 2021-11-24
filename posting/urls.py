from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.index, name="projects"),
    path('post-projects/', views.post_projects, name="post-projects")
]