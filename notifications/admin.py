from django.contrib import admin
from .models import NotificationJobs, NotificationProjects

class NotificationProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_project', 'sender', 'to_user', 'notification_type', 'text_preview', 'created', 'is_seen']

class NotificationJobsAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_job', 'sender', 'to_user', 'notification_type', 'text_preview', 'created', 'is_seen']

admin.site.register(NotificationProjects, NotificationProjectsAdmin)
admin.site.register(NotificationJobs, NotificationJobsAdmin)