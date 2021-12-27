from django.urls import path
from . import views

urlpatterns = [
    path('post-project/<int:project_id>', views.comment_project, name="comment-projects"),
    path('comment-post-project/<int:project_id>', views.post_comment_project, name="post-comment-project"),
    path('delete-comment-project/<int:comment_id>', views.delete_comment_project, name='delete-comment'),
    path('edit-comment/<int:comment_id>', views.edit_comment_project, name='edit-comment'),

    path('post-job/<int:jobs_id>', views.comment_jobs, name="comment-jobs"),
    path('comment-post-job/<int:jobs_id>', views.post_comment_jobs, name="post-comment-jobs"),
    path('delete-comment-job/<int:comment_id>', views.delete_comment_jobs, name='delete-comment-jobs'),
    path('edit-comment-job/<int:comment_id>', views.edit_comment_jobs, name='edit-comment-jobs'),
]