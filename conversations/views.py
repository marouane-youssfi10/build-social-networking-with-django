from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
from accounts.models import Account
from django.db.models import Max, Min, Count
from django.db.models import Subquery, OuterRef, F
from django.db.models import Q
def inbox(request):
    # get all message of users  who send message
    messages_users = Message.objects.all() # .exclude(user=request.user)

    messages_users = messages_users.filter(Q(recipient=request.user)| Q(sender=request.user)).order_by('user', '-created').distinct('user')
    # print('messages_users = ', messages_users)
    print('---------------------------------')
    for i in messages_users:
        print('i.user      = ', i.user)
        print('i.sender    = ', i.sender)
        print('i.recipient = ', i.recipient)
        print('i.body      = ', i.body)
        print('i.updated   = ', i.updated)
        print('---------------------------------')
    print()
    users = []
    for message_user in messages_users:
        users.append({
            'user': message_user.user,
            'sender': message_user.sender,
            'recipient': message_user.recipient,
            'body': message_user.body,
            'created': message_user.created,
            'updated': message_user.updated,
            'is_read': message_user.is_read,
            'count': Message.objects.filter(user=request.user, sender=message_user.sender, recipient=message_user.recipient, is_read=False).count()
        })
    # print(messages_users, '\n --------------- ')
    # print(users)
    for i in users:
        print(i['user'], ' - ', i['body'], ' - ', i['count'])

    context = {
        'messages_users': messages_users,
        'users': users,
    }
    return render(request, 'conversations/messages.html', context)

def conversations(request, message_user_id):
    # # get all message of users  who send message
    Message.objects.filter(id=message_user_id, is_read=False).update(is_read=True)
    # NotificationProjects.objects.filter(to_user=request.user, is_seen=False).update(is_seen=True)
    messages_users = Message.objects.all()
    messages_users = messages_users.filter(Q(recipient=request.user) | Q(sender=request.user)).order_by('user', '-updated').distinct('user')
    to_user = Message.objects.get(id=message_user_id)
    print('to_user = ', to_user)

    conversations = Message.objects.filter(user=request.user)
    conversations = conversations.filter(sender=request.user, recipient=to_user.user).order_by('updated') | conversations.filter(sender=to_user.user, recipient=request.user).order_by('updated')

    context = {
        'messages_users': messages_users,
        'conversations': conversations,
        'to_user': to_user,
    }
    return render(request, 'conversations/messages.html', context)