from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:project_id>', views.comment_project, name="comment"),
    path('comment_post_project/<int:project_id>', views.post_comment_project, name="post-comment-project"),
    path('delete_comment_project/<int:comment_id>', views.delete_comment_project, name='delete-comment'),
    path('edit_comment/<int:comment_id>', views.edit_comment_project, name='edit-comment'),

    path('post_jobs/<int:jobs_id>', views.comment_jobs, name="comment-jobs"),
    path('comment_post_jobs/<int:jobs_id>', views.post_comment_jobs, name="post-comment-jobs"),
    path('delete_comment_jobs/<int:comment_id>', views.delete_comment_jobs, name='delete-comment-jobs'),
    ]