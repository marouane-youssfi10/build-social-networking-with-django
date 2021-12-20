from django.db import models
# models
from posting.models import PostProject, PostJobs

class CommentProjects(models.Model):
    post_project = models.ForeignKey(PostProject, on_delete=models.CASCADE, related_name='post_project_comment')
    user_post = models.ForeignKey("accounts.Account", on_delete=models.CASCADE,  related_name='user_post')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_post)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment Projects'
        ordering = ['-updated']

class CommentJobs(models.Model):
    post_job = models.ForeignKey(PostJobs, on_delete=models.CASCADE, related_name='post_job_comment')
    user_job = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='user_job')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_job)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment Jobs'
        ordering = ['-updated']