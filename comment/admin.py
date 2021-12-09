from django.contrib import admin
from .models import CommentJobs, CommentProjects

class CommentProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_project', 'user_post', 'body', 'created', 'updated')

class CommentJobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'jobs_profile', 'user_job', 'body', 'created', 'updated')

admin.site.register(CommentProjects, CommentProjectsAdmin)
admin.site.register(CommentJobs, CommentJobsAdmin)