from django.shortcuts import render
from .models import NotificationProjects

def show_notifications(request):
    notifications = NotificationProjects.objects.filter(to_user=request.user)
    NotificationProjects.objects.filter(to_user=request.user, is_seen=False).update(is_seen=True)

    print('\nnotifications = ', notifications, '\n')
    context = {
        'notifications': notifications
    }
    return render(request, 'notifications/notifications.html', context)


