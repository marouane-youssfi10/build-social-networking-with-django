from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
# models
from posting.models import PostProject
from .models import NotificationProjects

# @receiver(m2m_changed, sender=PostProject.likes.through)
"""@receiver(post_save, sender=PostProject)
def send_like_notifications(sender, instance, created, **kwargs):
    print('==============================================================')
    print('sender                  = ', sender)
    print('created                 = ', created)

    # kana5do user dyal dik lpost
    # post = user.post_project
    post = instance
    last_one = post.likes.all()
    user = post.likes.last()
    print('last_one                = ', last_one.last())
    print('post                    = ', post.likes)
    print('like.user               = ', post.user)
    print('like.post_project.user  = ', user)

    # notify = NotificationProjects(post_project=post, sender=sender, to_user=post.user, notification_type=1)
    # notify.save()"""
@receiver(m2m_changed, sender=PostProject.likes.through)
def m2m_changed_likes(sender, instance, action, model, pk_set, **kwargs):
    print('pk_set        = ', pk_set)
    print('model         = ', model.user)
    print('sender        = ', sender)
    print('instance      = ', instance)
    print('instance.user = ', instance.user)
    print('instance.user = ', instance.likes.all())
    print('action        = ', action)
    print('------------------------------------')


"""
NOTIFICATION_TYPES  ,post_project ,sender  ,to_user ,notification_type ,text_preview ,created
"""