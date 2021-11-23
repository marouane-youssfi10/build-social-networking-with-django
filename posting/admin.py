from django.contrib import admin
from .models import PostProject, TagsProjects
# Register your models here.

class TagsProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tags_users_projects', 'tag')

class PostProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'name_project', 'start_price', 'end_price')
    readonly_fields = ('created_project', 'updated_project')

admin.site.register(PostProject, PostProjectAdmin)
admin.site.register(TagsProjects, TagsProjectsAdmin)
