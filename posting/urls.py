from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.index, name="projects"),
    path('post-project/', views.post_projects, name="post-project"),
    path('jobs/', views.post_job, name="post-job"),
    path('projects/search/', views.search, name="search"),
    path('projects/filter/', views.filter_project, name="filter"),
]