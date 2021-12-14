from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'sender', 'recipient', 'body', 'created', 'is_read']
    list_editable = ['is_read']

admin.site.register(Message, MessageAdmin)
