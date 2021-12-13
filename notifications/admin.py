from django.contrib import admin
from .models import NotificationJobs, NotificationProjects

class NotificationProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_project', 'to_user', 'notification_type', 'sender', 'body', 'created', 'is_seen']
    list_editable = ['is_seen']

class NotificationJobsAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_job', 'to_user', 'notification_type', 'sender', 'body', 'created', 'is_seen']
    list_editable = ['is_seen']

admin.site.register(NotificationProjects, NotificationProjectsAdmin)
admin.site.register(NotificationJobs, NotificationJobsAdmin)