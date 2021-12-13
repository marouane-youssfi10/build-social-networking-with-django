from .models import NotificationProjects
from accounts.models import Account

def show_notifications(request):
    if request.user.is_authenticated:
        user = request.user
        notifications = NotificationProjects.objects.filter(sender=user)
        # NotificationProjects.objects.filter(sender=user, is_seen=False).update(is_seen=True)
        return dict(notifications=notifications)
