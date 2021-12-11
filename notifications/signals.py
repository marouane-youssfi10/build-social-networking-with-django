from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
# models
from posting.models import PostProject
from .models import NotificationProjects
from accounts.models import Account

# @receiver(m2m_changed, sender=PostProject.likes.through)
"""@receiver(post_save, sender=PostProject)
def send_like_notifications(sender, instance, created, **kwargs):

    # notify = NotificationProjects(post_project=post, sender=sender, to_user=post.user, notification_type=1)
    # notify.save()"""
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
        if NotificationProjects.objects.filter(post_project=user_post, sender=request_user, to_user=to_user).exists():
            print('------ exists -----')
            pass
        else:
            if to_user != request_user:
                #                               PostProject             Account              Account
                notify = NotificationProjects(post_project=user_post, sender=request_user, to_user=to_user, notification_type=1)
                notify.save()

"""
NOTIFICATION_TYPES  ,post_project ,sender  ,to_user ,notification_type ,text_preview ,created
post_project : noti_post_project
sender       : noti_project_from_user | me
to_user      : noti_project_to_user   | to
"""