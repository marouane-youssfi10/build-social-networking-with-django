from django.contrib import admin
from .models import UserProfile, Account
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'experience', 'education_title', 'location_country', 'location_city',
                   'links_media', 'experience']
    prepopulated_fields = {'slug': ('user',)}

class AccountAdmin(UserAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="60" height="60" style="border-radius: 50px;" />'.format(object.photo_profile.url))

    list_display = ('id', 'email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active', 'thumbnail')
    list_display_links = ('id', 'email', 'first_name', 'last_name', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Account, AccountAdmin)
