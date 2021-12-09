from django.contrib import admin
from .models import CommentJobs, CommentProjects

class CommentProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'body')

class CommentJobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'jobs', 'user', 'body')

admin.site.register(CommentProjects, CommentProjectsAdmin)
admin.site.register(CommentJobs, CommentJobsAdmin)