from django.db.models.signals import post_save
from django.dispatch import receiver
# models
from .models import Account, UserProfile
from user_profile.models import Experience_user, TagsUser, Social_media
from follow.models import Follow

@receiver(post_save, sender=Account)
def post_save_create_user_profile_and_user_follow(sender, instance, created, **kwargs):
    if created:
        user = instance
        # create user into Experience_user
        experience_user = Experience_user()
        experience_user.experience_user_id = user.id
        experience_user.save()

        # create user into Social_media
        social_media = Social_media()
        social_media.social_media_user_id = user.id
        social_media.save()

        # create user into Tags
        tags = TagsUser()
        tags.tags_user_id = user.id
        tags.save()

        # create user into UserProfile
        user_profile = UserProfile.objects.create(
            user=user, slug=user.id,
            experience=experience_user,
            links_media=social_media,
        )
        user_profile.save()

        # create user into Follow app
        follow = Follow.objects.create(
            user=user
        )
        follow.save()