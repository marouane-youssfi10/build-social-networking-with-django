from django.db import models
from accounts.models import Account


class Follow(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='follow_user')
    following = models.ManyToManyField(Account,  blank=True, related_name='following')
    followers = models.ManyToManyField(Account, blank=True, related_name='followers')

    class Meta:
        verbose_name = 'Follow'
        verbose_name_plural = 'Follow'

    def __str__(self):
        return str(self.user)

