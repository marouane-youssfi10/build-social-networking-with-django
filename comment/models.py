from django.db import models
# models
from posting.models import PostProject

class CommentProjects(models.Model):
    post_project = models.ForeignKey(PostProject, on_delete=models.CASCADE, related_name='post_project')
    user_post = models.ForeignKey("accounts.Account", on_delete=models.CASCADE,  related_name='user_post')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_post)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment Projects'
        ordering = ['-date']

class CommentJobs(models.Model):
    jobs_profile = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, related_name='jobs_profile')
    user_job = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='user_job')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'jobs_profile : ' + str(self.jobs_profile) + ' -- user_job : ' +str(self.user_job) + ' -- ' + str(self.body)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment Jobs'