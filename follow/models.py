from django.db import models
from accounts.models import Account


class Follow(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    followers = models.ManyToManyField(Account,  blank=True, related_name='followers')
    following = models.ManyToManyField(Account,  blank=True, related_name='following')

    class Meta:
        verbose_name = 'Follow'
        verbose_name_plural = 'Follow'