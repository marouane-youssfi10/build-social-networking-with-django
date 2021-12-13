from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
# models
from posting.models import PostProject
from .models import NotificationProjects
from accounts.models import Account, UserProfile
from comment.models import CommentProjects
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
def post_save_comment(instance, **kwargs):
    user = instance
    user_post = user.post_project
    request_user = user.user_post
    to_user = user.post_project.user
    body = user.body

    if not NotificationProjects.objects.filter(post_project=user_post, sender=request_user, to_user=to_user, body=body, notification_type=2).exists():
        """ avoid save into NotificationProjects request_user == to_user for not showing noti
        to your profile with like or comment your profile """
        if to_user != request_user:
            notify = NotificationProjects(post_project=user_post,
                                          sender=request_user,
                                          to_user=to_user,
                                          body=body,
                                          notification_type=2)
            notify.save()

@receiver(m2m_changed, sender=Follow.following.through)
def post_save_follow(instance, action, pk_set, **kwargs):
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
@receiver(m2m_changed, sender=UserProfile.likes.through)
def m2m_changed_likes_project(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        user_post = instance.user.user_profile
        to_user = instance.user
        request_user_id = list(pk_set)[0]
        request_user = Account.objects.get(id=request_user_id)
        print('user_post       = ', user_post)
        print('to_user         = ', to_user)
        print('request_user_id = ', request_user_id)
        print('request_user    = ', request_user)
        if not NotificationProjects.objects.filter(post_job=user_post, sender=request_user, to_user=to_user, notification_type=1).exists():
            if to_user != request_user:
                notify = NotificationProjects(post_job=user_post, sender=request_user, to_user=to_user,
                                            notification_type=1)
                notify.save()


# NOTIFICATION_TYPES  ,post_project ,sender  ,to_user ,notification_type ,text_preview ,created
# post_project : noti_post_project
# sender       : noti_project_from_user | me
# to_user      : noti_project_to_user   | to
