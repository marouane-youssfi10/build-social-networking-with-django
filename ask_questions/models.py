from django.db import models
from accounts.models import Account
# Create your models here.

class TagsQuestions(models.Model):
    tags_user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tag users'

    def __str__(self):
        return self.tag if self.tag else ''

class Ask_questions(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='user_ask')
    question = models.CharField(max_length=100)

    created_question = models.DateTimeField(auto_now_add=True)
    updated_question = models.DateTimeField(auto_now=True)

    tag_question = models.ManyToManyField(TagsQuestions, blank=True, related_name='tag_question')
    likes = models.ManyToManyField(Account, blank=True, related_name='likes_question')
    viewers = models.ManyToManyField(Account, blank=True, related_name='viewers_questions')

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'Ask_questions'

    def __str__(self):
        return self.question