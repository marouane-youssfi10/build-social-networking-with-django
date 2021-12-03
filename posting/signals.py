from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PostProject, TagsProjects


"""@receiver(post_save, sender=PostProject)
def post_save_create_tags_post(sender, instance, created, **kwargs):
    print('------------------ post_save_create_tags_post ------------------')
    print('sender = ', sender)
    print('instance = ', instance)
    print('instance.user = ', instance.user)
    print('instance.id = ', instance.id)
    if created:
        user_id = instance.id
        tags_project_post = TagsProjects.objects.last()
        print('tags_project_post                     = ', tags_project_post)
        print('tags_project_post.tag                 = ', tags_project_post.tag)
        print('tags_project_post.tags_users_projects = ', tags_project_post.tags_users_projects)
        print('tags_project_post.id = ', tags_project_post.id)
        print('------------------------------------')

        post_project = PostProject.objects.get(id=user_id)
        post_project.skills_tags_projects.set(tags_project_post.tags_users_projects)
        post_project.save()"""
