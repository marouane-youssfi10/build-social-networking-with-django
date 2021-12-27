from django.db import models


class TagsProjects(models.Model):
    tags_users_projects = models.ForeignKey("accounts.Account", on_delete=models.CASCADE,  related_name='tags_users_projects')
    tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'tags Projects'
        verbose_name_plural = 'TagsUsers Projects'

    def __str__(self):
        return self.tag if self.tag else ''

class TagsJobs(models.Model):
    tags_users_jobs = models.ForeignKey("accounts.Account", on_delete=models.CASCADE,  related_name='tags_users_jobs')
    tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'tags jobs'
        verbose_name_plural = 'TagsUsers jobs'

    def __str__(self):
        return self.tag if self.tag else ''

class PostProject(models.Model):
    user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='user')
    name_project = models.CharField(max_length=100, blank=False, null=False)
    epic_coder = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    start_price = models.IntegerField(blank=False, null=False)
    end_price = models.IntegerField(blank=False, null=False)
    description_project = models.TextField(blank=False, null=False)
    hide = models.BooleanField(default=False)

    updated_project = models.DateTimeField(auto_now=True)
    created_project = models.DateTimeField(auto_now_add=True)

    skills_tags_projects = models.ManyToManyField(TagsProjects, blank=True)
    likes = models.ManyToManyField("accounts.Account", blank=True, related_name='likes_post_projects')
    viewers_project = models.ManyToManyField("accounts.Account", blank=True, related_name='viewers_project')

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_project']

    def __str__(self):
        return self.name_project

class PostJobs(models.Model):
    STATUS_CHOICES = (
        (1, 'Select Type Work'),
        ('Hourly', 'Hourly'),
        ('Part time', 'Part time'),
        ('Full time', 'Full time'),
    )
    user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='job')
    name_jobs = models.CharField(max_length=100, blank=False, null=False)
    type_work_job = models.CharField(choices=STATUS_CHOICES, max_length=100, blank=False, null=False, default=1)
    epic_coder = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    description_job = models.TextField(blank=False, null=False)
    hide = models.BooleanField(default=False)

    updated_job = models.DateTimeField(auto_now=True)
    created_job = models.DateTimeField(auto_now_add=True)

    skills_tags_jobs = models.ManyToManyField(TagsJobs, blank=True)
    likes = models.ManyToManyField("accounts.Account", blank=True, related_name='likes_post_jobs')
    viewers_job = models.ManyToManyField("accounts.Account", blank=True, related_name='viewers_job')

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-created_job']

    def __str__(self):
        return str(self.user)
