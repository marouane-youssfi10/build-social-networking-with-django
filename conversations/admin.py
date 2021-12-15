from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'recipient', 'body', 'created', 'is_read']
    list_filter = ['user', 'recipient']
    list_editable = ['is_read']

admin.site.register(Message, MessageAdmin)
