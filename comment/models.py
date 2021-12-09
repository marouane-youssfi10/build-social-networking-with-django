from django.db import models
# models
from accounts.models import Account
from posting.models import PostProject


class Comment(models.Model):
    post = models.ForeignKey(PostProject, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)