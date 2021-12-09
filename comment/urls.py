from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:project_id>', views.comment, name="comment"),
    path('comment_post_project/<int:project_id>', views.post_comment_project, name="post-comment-project"),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete-comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit-comment'),

    path('comment_post_jobs/<int:project_id>', views.post_comment_jobs, name="post-comment-jobs"),
    ]