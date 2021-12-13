from django.contrib import admin
from .models import CommentJobs, CommentProjects

class CommentProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_project', 'body', 'user_post', 'created', 'updated')

class CommentJobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'jobs_profile', 'body', 'user_job', 'created', 'updated')

admin.site.register(CommentProjects, CommentProjectsAdmin)
admin.site.register(CommentJobs, CommentJobsAdmin)