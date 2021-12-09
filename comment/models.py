from django.db import models
# models
from accounts.models import Account, UserProfile
from posting.models import PostProject

class CommentProjects(models.Model):
    post = models.ForeignKey(PostProject, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class CommentJobs(models.Model):
    jobs = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)