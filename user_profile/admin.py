from django.contrib import admin
from .models import TagsUser, Experience_user, Social_media
# Register your models here.

class TagsUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'tags_user', 'tag')

class ExperienceUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'experience_user', 'experince_title', 'experince_description')

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'social_media_user', 'name', 'link')

admin.site.register(TagsUser, TagsUserAdmin)
admin.site.register(Experience_user, ExperienceUserAdmin)
admin.site.register(Social_media, SocialMediaAdmin)
