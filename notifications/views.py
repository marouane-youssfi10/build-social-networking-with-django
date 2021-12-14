from django.shortcuts import render
from .models import NotificationProjects
from accounts.models import UserProfile
from posting.models import PostProject

def show_notifications(request):
    notifications = NotificationProjects.objects.filter(to_user=request.user)

    context = {
        'notifications': notifications
    }
    response = render(request, 'notifications/notifications.html', context)
    NotificationProjects.objects.filter(to_user=request.user, is_seen=False).update(is_seen=True)
    return response

def count_notifications(request):
    count_notifications = 0

    if request.user.is_authenticated:
        request_user_profile = UserProfile.objects.get(id=request.user.id)
        request_user_postproject = PostProject.objects.filter(user=request.user)
        ids = request_user_postproject.values_list('pk', flat=True)
        ids = list(ids)

        count_notifications_projects = NotificationProjects.objects.filter(post_project__in=ids, is_seen=False).count()
        count_notifications_jobs = NotificationProjects.objects.filter(post_job=request_user_profile, is_seen=False).count()
        count_notifications = int(count_notifications_projects) + int(count_notifications_jobs)

    return {'count_notifications': count_notifications}



