from django.contrib import admin
from .models import TagsUser, Experience_user, Social_media
# Register your models here.

class TagsUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')

class ExperienceUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'experince_title', 'experince_description')

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')

admin.site.register(TagsUser, TagsUserAdmin)
admin.site.register(Experience_user, ExperienceUserAdmin)
admin.site.register(Social_media, SocialMediaAdmin)
