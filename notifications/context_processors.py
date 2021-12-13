from .models import NotificationProjects
from accounts.models import Account
"""
def show_notifications(request):
    if 'admin' in request.path:
        return {}

    if request.user is None:
        print(' ---- request.user is None ---- ')

    if request.user.is_authenticated:
        print('\n---- show_notifications ----\n')
        user = request.user
        notifications = NotificationProjects.objects.filter(sender=user)
        # NotificationProjects.objects.filter(sender=user, is_seen=False).update(is_seen=True)
        return dict(notifications=notifications)"""
