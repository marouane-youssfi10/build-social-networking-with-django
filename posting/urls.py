from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.index, name="projects"),
    path('post-project/', views.post_projects, name="post-project"),
    path('jobs/', views.post_job, name="post-job"),
    path('projects/search/', views.search, name="search"),
    path('projects/filter/', views.filter_project, name="filter"),

    path('projects/edit-post/<int:pk>/', views.edit_post_project, name="edit-post-project"),

    path('projects/delete-tag-post/<int:pk>/<int:project_post_id>/', views.delete_tag_post, name="delete-tag-post"),
    path('projects/create-tag-post/<int:project_post_id>/', views.create_tags_post, name="create-tags-post")

]