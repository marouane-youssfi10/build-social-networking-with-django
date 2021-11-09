from django.contrib import admin
from .models import UserProfile, Account, Tags, Experience_user
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="60" style="border-radius: 50px;" />'.format(object.photo_profile.url))

    list_display = ['user', 'education_title', 'education_year_start', 'education_year_end',
                    'location_country', 'location_city', 'hourly_work', 'type_work', 'thumbnail']

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')

class ExperienceUserAdmin(admin.ModelAdmin):
    list_display = ('experince_user', 'experince_title', 'experince_description')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Experience_user, ExperienceUserAdmin)