from django.shortcuts import render, redirect
from .models import Message
from django.db.models import Q
from django.http import HttpResponse

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
    to_user = {'id': 0, 'name': 'test'}
    context = {
        'users': users,
        'to_user': to_user,
    }
    return render(request, 'conversations/messages.html', context)

def conversations(request, message_user_id):
    print('------- 1 -------')
    # # get all message of users  who send message
    message_user = Message.objects.get(id=message_user_id)
    print('------- 2 -------')
    # check if message_user.user == message_user.sender for modified is_read to true.
    if message_user.user == message_user.sender:
        Message.objects.filter(sender=message_user.sender, recipient=message_user.recipient, is_read=False).update(is_read=True)
    print('------- 3 -------')

    # get all Message
    messages_users = Message.objects.all()
    print('------- 4 -------')
    # filter message with request.user whatever in sender or recipient
    messages_users = messages_users.filter(Q(recipient=request.user) | Q(sender=request.user)).order_by('user', '-created').distinct('user')
    users = [] # create list named users for storing data plus count message no reading
    for message_user in messages_users:
        # filtering with getting rows with is_read false message
        count = Message.objects.filter(
            user=request.user, sender=message_user.sender,
            recipient=message_user.recipient, is_read=False
        ).count()
        # append users data
        users.append({
            'id': message_user.id, 'user': message_user.user, 'sender': message_user.sender, 'recipient': message_user.recipient,
            'body': message_user.body, 'created': message_user.created, 'updated': message_user.updated,'is_read': message_user.is_read,
            'count': count
        })
    # to_user for active background color when the user read the conversations
    to_user = Message.objects.get(id=message_user_id)

    # get all conversations between you and the user want him
    conversations = Message.objects.filter(user=request.user)
    conversations = conversations.filter(sender=request.user, recipient=to_user.user).order_by('created') | conversations.filter(sender=to_user.user, recipient=request.user).order_by('created')

    context = {
        'users': users,
        'conversations': conversations,
        'to_user': to_user,
        'the_user': message_user
    }
    return render(request, 'conversations/messages.html', context)

def send_message(request, to_user):
    the_user = Message.objects.get(id=to_user)

    if request.POST:
        body = request.POST['send_message']
        # Message.objects.create(user=request.user, sender=, recipient=, body=body, is_read=False)
        print('request.user = ', request.user)
        print('the_user     = ', the_user)
        return redirect(request.META.get('HTTP_REFERER'))
