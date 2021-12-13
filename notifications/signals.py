from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
# models
from posting.models import PostProject
from .models import NotificationProjects
from accounts.models import Account
from comment.models import CommentProjects

@receiver(m2m_changed, sender=PostProject.likes.through)
def m2m_changed_likes(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        user_post = instance
        to_user = instance.user
        request_user_id = list(pk_set)[0]
        request_user = Account.objects.get(id=request_user_id)
        print('to_user         = ', to_user)
        print('request_user_id = ', request_user_id)
        print('request_user    = ', request_user)
        if not NotificationProjects.objects.filter(post_project=user_post, sender=request_user, to_user=to_user).exists():
            if to_user != request_user:
                notify = NotificationProjects(post_project=user_post, sender=request_user, to_user=to_user,
                                            notification_type=1)
                notify.save()

@receiver(post_save, sender=CommentProjects)
def post_save_comment(sender, instance, **kwargs):
    user = instance
    print('------------------------------------')
    print('sender                       = ', sender)
    print('user                         = ', user)
    print('user.post_project.user       = ', user.post_project.user)
    print('user.user_post               = ', user.user_post)
    print('user.post_project            = ', user.post_project)
    print('instance.body                = ', user.body)
    print('------------------------------------')
    user_post = user.post_project
    request_user = user.user_post
    to_user = user.post_project.user
    body = user.body

    if not NotificationProjects.objects.filter(post_project=user_post, sender=request_user, to_user=to_user, body=body).exists():
        """ avoid save into NotificationProjects request_user == to_user for not showing noti
        to your profile with like or comment your profile """
        if to_user != request_user:
            notify = NotificationProjects(post_project=user_post,
                                          sender=request_user,
                                          to_user=to_user,
                                          body=body,
                                          notification_type=2)
            notify.save()

"""
NOTIFICATION_TYPES  ,post_project ,sender  ,to_user ,notification_type ,text_preview ,created
post_project : noti_post_project
sender       : noti_project_from_user | me
to_user      : noti_project_to_user   | to
"""