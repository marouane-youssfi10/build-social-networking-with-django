from django.urls import path
from . import views


urlpatterns = [
    path('post_comment/', views.post_comment, name="post-comment")
    ]