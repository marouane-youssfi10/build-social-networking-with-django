from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
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

def conversations(request, recipient_id):
    print('recipient_id  = ', recipient_id)
    print('recipient_id  = ', Message.objects.get(id=recipient_id))
    print('request.user = ', request.user)
    to_user = Message.objects.get(id=recipient_id)
    messages_users = Message.objects.filter(recipient=request.user).exclude(user=request.user)
    conversations = Message.objects.filter(user=request.user)
    conversations = conversations.filter(sender=request.user, recipient=to_user.user) | conversations.filter(sender=to_user.user, recipient=request.user)
    for i in conversations:
        print('user = ', i.user, '| sender =', i.sender, '| recipient = ', i.recipient, '| body = ', i.body)
    context = {
        'messages_users': messages_users,
        'conversations': conversations,
        'to_user': to_user,
    }
    return render(request, 'conversations/messages.html', context)