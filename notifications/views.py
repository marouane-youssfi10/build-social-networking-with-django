from django.shortcuts import render
from .models import NotificationProjects

def Show_notifications(request):
    user = request.user
    notifications = NotificationProjects.objects.filter(sender=user).order_by('-created')
    NotificationProjects.objects.filter(sender=user, is_seen=False).update(is_seen=True)

    context = {
        'notifications': notifications
    }
    # return render(request, 'includes/navbar.html', context)


