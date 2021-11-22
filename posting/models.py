from django.db import models
from accounts.models import Account, UserProfile


class TagsProjects(models.Model):
    tags_users_projects = models.ForeignKey(Account, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'tagsProjects'
        verbose_name_plural = 'TagsUserProjects'

    def __str__(self):
        return self.tag if self.tag else ''

class PostProject(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name_project = models.CharField(max_length=100, blank=False, null=False)
    start_price = models.CharField(max_length=100, blank=False, null=False)
    end_price = models.CharField(max_length=100, blank=False, null=False)
    description_project = models.TextField(blank=False, null=False)

    skills_tags_projects = models.ManyToManyField(TagsProjects, blank=False, null=False)

    def __str__(self):
        return self.name_project
