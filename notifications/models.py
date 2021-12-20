from django.db import models
# models
from accounts.models import Account, UserProfile
from posting.models import PostProject, PostJobs

class NotificationProjects(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'))
    post_job = models.ForeignKey(PostJobs, on_delete=models.CASCADE, related_name='noti_post_job', blank=True, null=True)
    post_project = models.ForeignKey(PostProject, on_delete=models.CASCADE, related_name='noti_post_project', blank=True, null=True)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='noti_project_from_user')
    to_user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='noti_project_to_user')
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return str(self.sender)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notification Projects Jobs'
        ordering = ['-created']