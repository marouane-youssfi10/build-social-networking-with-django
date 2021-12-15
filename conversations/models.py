from django.db import models
from accounts.models import Account


class Message(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_message', blank=True)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='from_user', blank=True, null=True)
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='to_user', blank=True, null=True)
    body = models.TextField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering = ['-created', '-updated']