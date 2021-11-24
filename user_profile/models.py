from django.db import models

class TagsUser(models.Model):
    tags_user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tagUsers'

    def __str__(self):
        return self.tag if self.tag else ''

class Experience_user(models.Model):
    experience_user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    experince_title = models.CharField(max_length=100, null=True, blank=True)
    experince_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.experince_title if self.experince_title else ''

class Social_media(models.Model):
    STATUS_CHOICES = (
        ('facebook', 'facebook'),
        ('linkedin', 'linkedin'),
        ('instagram', 'instagram'),
        ('youtube', 'youtube'),
        ('twitter', 'twitter'),
        ('github', 'github'),
        ('pinterest', 'pinterest'),
    )

    social_media_user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True, choices=STATUS_CHOICES, default=None)
    link = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else ''

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links media'