from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:project_id>', views.comment, name="comment"),
    path('comment/', views.post_comment, name="post-comment_project"),
    path('comment/', views.post_comment, name="post-comment-jobs"),
    ]