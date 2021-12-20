from django.urls import path
from . import views

urlpatterns = [
    # page projects
    path('projects/', views.projects, name="projects"),
    path('post-project/', views.post_projects, name="post-project"),
    path('projects/search/', views.search_projects, name="search-projects"),
    path('projects/filter/', views.filter_project, name="filter-projects"),
    path('projects/edit-post/<int:pk>/', views.edit_post_project, name="edit-post-project"),
    path('projects/delete-tag-post/<int:pk>/<int:project_post_id>/', views.delete_tag_post_project, name="delete-tag-post"),
    path('projects/create-tag-post/<int:project_post_id>/', views.create_tags_post_project, name="create-tags-post"),
    path('hide/<int:pk>', views.hide_projects, name='hide'), # for hide projects
    path('unhide/<int:pk>', views.unhide_projects, name='unhide'), # for unhide projects


    # page Jobs
    path('jobs/', views.jobs, name="jobs"),
    path('post-job/', views.post_job, name="post-project"),
    path('jobs/search/', views.search_jobs, name="search-jobs"),
    path('jobs/filter/', views.filter_jobs, name="filter-jobs"),



]