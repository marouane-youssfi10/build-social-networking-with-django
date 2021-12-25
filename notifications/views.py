from django.shortcuts import render
from .models import NotificationProjects
from posting.models import PostProject, PostJobs
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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
        request_user_post_job = PostJobs.objects.filter(user__username=request.user.username)
        request_user_post_project = PostProject.objects.filter(user__username=request.user.username)

        # take the id of notifications currently user
        ids_job = request_user_post_job.values_list('pk', flat=True)
        ids_job = list(ids_job)


        ids_project = request_user_post_project.values_list('pk', flat=True)
        ids_project = list(ids_project)
        # get notifications "follow" not seeing and count them
        count_follow = NotificationProjects.objects.filter(to_user=request.user, notification_type=3, is_seen=False).count()

        # get all notifications "like, comment" not seeing and count them
        count_notifications_projects = NotificationProjects.objects.filter(post_project__in=ids_project, is_seen=False).count()
        count_notifications_jobs = NotificationProjects.objects.filter(post_job__in=ids_job, is_seen=False).count()
        count_notifications = int(count_notifications_projects) + int(count_notifications_jobs) + int(count_follow)


    return {'count_notifications': count_notifications}




