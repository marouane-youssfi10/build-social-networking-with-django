from django.urls import path
from . import views

urlpatterns = [
    # page projects
    path('projects/', views.projects, name="projects"),
    path('post-project/', views.post_projects, name="post-project"),
    path('post-project/delete/<int:project_id>', views.delete_post_projects, name="delete-post-project"),
    path('projects/search/', views.search_projects, name="search-projects"),
    path('projects/filter/', views.filter_project, name="filter-projects"),
    path('projects/edit-post/<int:pk>/', views.edit_post_project, name="edit-post-project"),
    path('projects/delete-tag-post/<int:pk>/<int:project_post_id>/', views.delete_tag_post_project, name="delete-tag-post"),
    path('projects/create-tag-post/<int:project_post_id>/', views.create_tags_post_project, name="create-tags-post"),
    path('projects/hide-post-project/<int:pk>/', views.hide_projects, name='hide-project'), # for hide projects
    path('projects/unhide-post-project/<int:pk>/', views.unhide_projects, name='unhide-project'), # for unhide projects

    # page Jobs
    path('jobs/', views.jobs, name="jobs"),
    path('post-job/', views.post_job, name="post-job"),
    path('post-job/delete/<int:job_id>', views.delete_post_jobs, name="delete-post-job"),
    path('jobs/edit-post/<int:pk>/', views.edit_post_job, name="edit-post-job"),
    path('jobs/delete-tag-post-job/<int:pk>/<int:job_post_id>/', views.delete_tag_post_job, name="delete-tag-post-job"),
    path('jobs/create-tag-post-job/<int:job_post_id>/', views.create_tags_post_job, name="create-tags-post-job"),
    path('jobs/search/', views.search_jobs, name="search-jobs"),
    path('jobs/filter/', views.filter_jobs, name="filter-jobs"),
    path('jobs/hide-post-job/<int:job_id>/', views.hide_jobs, name='hide-job'), # for hide projects
    path('jobs/unhide-post-job/<int:job_id>/', views.unhide_jobs, name='unhide-job'), # for unhide projects



]