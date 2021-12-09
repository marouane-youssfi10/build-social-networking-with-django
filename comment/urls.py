from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:project_id>', views.comment, name="comment"),
    path('comment_post_project/<int:project_id>', views.post_comment_project, name="post-comment-project"),
    path('comment_post_jobs/<int:project_id>', views.post_comment_jobs, name="post-comment-jobs"),
    ]