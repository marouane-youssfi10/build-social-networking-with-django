from django.shortcuts import render
from .models import Message

def inbox(request):
    messages_users = Message.objects.filter(recipient=request.user).exclude(user=request.user)

    for i in messages_users:
        print('i.user = ', i.user)
        print('i.sender = ', i.sender)
        print('i.recipient = ', i.recipient)

    context = {
        'messages_users': messages_users
    }
    return render(request, 'conversations/messages.html', context)

def conversations(request, pk):
    pass