from django.shortcuts import render
from .models import NotificationProjects

def show_notifications(request):
    notifications = NotificationProjects.objects.filter(to_user=request.user)

    context = {
        'notifications': notifications
    }
    response = render(request, 'notifications/notifications.html', context)
    NotificationProjects.objects.filter(to_user=request.user, is_seen=False).update(is_seen=True)
    return response



