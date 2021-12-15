from django.shortcuts import render
from .models import Message
from django.db.models import Q

def inbox(request):
    # get all message of users  who send message
    messages_users = Message.objects.all()
    messages_users = messages_users.filter(Q(recipient=request.user)| Q(sender=request.user)).order_by('user', '-created').distinct('user')

    users = []
    for message_user in messages_users:
        # print('messages_users.id = ', message_user.id)
        count = Message.objects.filter(
            sender=message_user.sender,
            recipient=message_user.recipient,
            is_read=False
        ).exclude(user=request.user).count()

        users.append({
            'id': message_user.id,
            'user': message_user.user,
            'sender': message_user.sender,
            'recipient': message_user.recipient,
            'body': message_user.body,
            'created': message_user.created,
            'updated': message_user.updated,
            'is_read': message_user.is_read,
            'count': count
        })
    # for i in users:
    #     print(i['user'], ' - ', i['body'], ' - ', i['count'])

    context = {
        'users': users,
    }
    return render(request, 'conversations/messages.html', context)

def conversations(request, message_user_id):
    # # get all message of users  who send message
    print('message_user_id = ', message_user_id)
    message_user = Message.objects.get(id=message_user_id)
    print('message_user.user = ', message_user.user)

    if message_user.user == message_user.sender:
        Message.objects.filter(sender=message_user.sender, recipient=message_user.recipient, is_read=False).update(is_read=True)

    messages_users = Message.objects.all()
    messages_users = messages_users.filter(Q(recipient=request.user) | Q(sender=request.user)).order_by('user', '-created').distinct('user')
    users = []
    for message_user in messages_users:
        count = Message.objects.filter(
            user=request.user, sender=message_user.sender,
            recipient=message_user.recipient, is_read=False
        ).count()
        users.append({
            'id': message_user.id, 'user': message_user.user, 'sender': message_user.sender, 'recipient': message_user.recipient,
            'body': message_user.body, 'created': message_user.created, 'updated': message_user.updated,'is_read': message_user.is_read,
            'count': count
        })
    to_user = Message.objects.get(id=message_user_id)
    # print('to_user = ', to_user)

    conversations = Message.objects.filter(user=request.user)
    conversations = conversations.filter(sender=request.user, recipient=to_user.user).order_by('created') | conversations.filter(sender=to_user.user, recipient=request.user).order_by('created')

    context = {
        'users': users,
        'conversations': conversations,
        'to_user': to_user,
    }
    return render(request, 'conversations/messages.html', context)