from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
# models
from posting.models import PostProject, PostJobs
from .models import NotificationProjects
from accounts.models import Account, UserProfile
from comment.models import CommentProjects, CommentJobs
from follow.models import Follow

# Projects
@receiver(m2m_changed, sender=PostProject.likes.through)
def m2m_changed_likes_project(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        user_post = instance
        to_user = instance.user
        request_user_id = list(pk_set)[0]
        request_user = Account.objects.get(id=request_user_id)
        if not NotificationProjects.objects.filter(post_project=user_post, sender=request_user, to_user=to_user, notification_type=1).exists():
            if to_user != request_user:
                notify = NotificationProjects(post_project=user_post, sender=request_user, to_user=to_user,
                                            notification_type=1)
                notify.save()

@receiver(post_save, sender=CommentProjects)
def post_save_comment_projects(instance, **kwargs):
    user = instance
    user_post = user.post_project
    request_user = user.user_post
    to_user = user.post_project.user
    body = user.body

    if not NotificationProjects.objects.filter(post_project=user_post, sender=request_user, to_user=to_user, body=body, notification_type=2).exists():
        """ avoid save into NotificationProjects request_user == to_user for not showing noti
        to your profile with like or comment"""
        if to_user != request_user:
            notify = NotificationProjects(post_project=user_post,
                                          sender=request_user,
                                          to_user=to_user,
                                          body=body,
                                          notification_type=2)
            notify.save()

# Follow
@receiver(m2m_changed, sender=Follow.following.through)
def post_save_follow_projects(instance, action, pk_set, **kwargs):
    if action == 'post_add':
        request_user = instance.user
        to_user_id = list(pk_set)[0]
        to_user = Account.objects.get(id=to_user_id)
        print('action       = ', action)
        print('request_user = ', request_user)
        print('to_user_id   = ', to_user_id)
        print('to_user      = ', to_user)
        if not NotificationProjects.objects.filter(sender=request_user, to_user=to_user, notification_type=3).exists():
            if to_user != request_user:
                notify = NotificationProjects(sender=request_user, to_user=to_user,
                                            notification_type=3)
                notify.save()

# Jobs
@receiver(m2m_changed, sender=PostJobs.likes.through)
def m2m_changed_likes_project(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        user_post = instance
        to_user = instance.user
        request_user_id = list(pk_set)[0]
        request_user = Account.objects.get(id=request_user_id)
        if not NotificationProjects.objects.filter(post_job=user_post, sender=request_user, to_user=to_user, notification_type=1).exists():
            if to_user != request_user:
                notify = NotificationProjects(post_job=user_post, sender=request_user, to_user=to_user,
                                            notification_type=1)
                notify.save()

@receiver(post_save, sender=CommentJobs)
def post_save_comment_jobs(instance, **kwargs):
    user = instance
    user_post = user.post_job
    request_user = user.user_job
    to_user = user.post_job.user
    body = user.body
    if not NotificationProjects.objects.filter(post_job=user_post, sender=request_user, to_user=to_user, body=body, notification_type=2).exists():
        """ avoid save into NotificationProjects request_user == to_user for not showing notification
        to your profile with like or comment"""
        if to_user != request_user:
            notify = NotificationProjects(post_job=user_post,
                                          sender=request_user,
                                          to_user=to_user,
                                          body=body,
                                          notification_type=2)
            notify.save()