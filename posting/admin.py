from django.contrib import admin
from .models import PostProject, PostJobs, TagsProjects, TagsJobs
# Register your models here.

class TagsProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tags_users_projects', 'tag')

class TagsJobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tags_users_jobs', 'tag')


class PostProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name_project', 'epic_coder', 'location', 'start_price', 'end_price', 'hide')
    readonly_fields = ('created_project', 'updated_project')

class PostJobAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name_jobs', 'epic_coder', 'type_work_job', 'location', 'price', 'hide')
    readonly_fields = ('created_job', 'updated_job')

# projects
admin.site.register(PostProject, PostProjectAdmin)
admin.site.register(TagsProjects, TagsProjectsAdmin)

# jobs
admin.site.register(PostJobs, PostJobAdmin)
admin.site.register(TagsJobs, TagsJobsAdmin)