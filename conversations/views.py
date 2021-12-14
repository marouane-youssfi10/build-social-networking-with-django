from django.shortcuts import render
from .models import Message

def inbox(request):
    messages = Message.objects.filter(recipient=request.user).exclude(user=request.user)

    for i in messages:
        print('i.user = ', i.user)
        print('i.sender = ', i.sender)
        print('i.recipient = ', i.recipient)

    context = {
        'messages': messages
    }
    return render(request, 'conversations/messages.html', context)