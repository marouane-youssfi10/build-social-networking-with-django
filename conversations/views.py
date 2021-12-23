from django.shortcuts import render, redirect
from .models import Message
from django.db.models import Q
from django.http import HttpResponse
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
def inbox(request):
    print('-------- inbox --------')
    # get all message of users  who send message
    messages_users = Message.objects.all()
    messages_users = messages_users.filter(Q(recipient=request.user)| Q(sender=request.user)).order_by('user', '-updated').distinct('user')

    users = []
    for message_user in messages_users:
        # filtering with getting rows with others users with counting how messages sending unreading
        count = Message.objects.filter(
            sender=message_user.sender,
            recipient=message_user.recipient,
            is_read=False
        ).exclude(user=request.user).count()
        # append to users data
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

    # sort data from max to min by date
    users = sorted(users, key=lambda x: x['updated'], reverse=True)

    # initializing to_user when redirect to page message for start a conversations
    to_user = {'id': 0, 'name': 'test'}
    context = {
        'users': users,
        'to_user': to_user,
    }
    return render(request, 'conversations/messages.html', context)

def conversations(request, message_user, message_user_id):
    print('-------- conversations --------')
    # # get all message of users  who send message
    message_user = Message.objects.get(id=message_user_id)
    # check if message_user.user == message_user.sender for modified is_read to true.
    if message_user.user == message_user.sender:
        Message.objects.filter(sender=message_user.sender, recipient=message_user.recipient, is_read=False).update(is_read=True)

    # get all Message
    messages_users = Message.objects.all()
    # filter message with request.user whatever in sender or recipient
    messages_users = messages_users.filter(Q(recipient=request.user) | Q(sender=request.user)).order_by('user', '-updated').distinct('user')

    # create list named users for storing data plus count message no reading
    users = []
    for message_user in messages_users:
        # filtering with getting rows with is_read false message
        count = Message.objects.filter(
            user=request.user, sender=message_user.sender,
            recipient=message_user.recipient, is_read=False
        ).count()
        # append data to users
        users.append({
            'id': message_user.id, 'user': message_user.user, 'sender': message_user.sender, 'recipient': message_user.recipient,
            'body': message_user.body, 'created': message_user.created, 'updated': message_user.updated, 'is_read': message_user.is_read,
            'count': count
        })

    # sort data from max to min by date
    users = sorted(users, key=lambda x: x['updated'], reverse=True)

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
    print('-------- send_message --------')
    the_user = Message.objects.get(id=to_user)

    if request.POST:
        body = request.POST['send_message']
        # create two message with different user and the same sender & recipient & body plus unreading
        Message.objects.create(user=request.user, sender=request.user, recipient=the_user.user, body=body, is_read=False)
        Message.objects.create(user=the_user.user, sender=request.user, recipient=the_user.user, body=body, is_read=False)
        return redirect(request.META.get('HTTP_REFERER'))

def add_user_to_conversation(request, pk):
    print('--------------- add_user_to_conversation ---------------')
    user_profile = UserProfile.objects.get(id=pk)

    var = Message.objects.filter(
        Q(user=request.user, sender=user_profile.user) | Q(user=request.user, recipient=user_profile.user))
    users = []

    for i in var:
        users.append(i.sender)

    if str(user_profile.user) in str(users):
        # get the last user message to redirect to conversations page with him
        user_profile_id = Message.objects.filter(user=user_profile.user).latest('user')
        return redirect('conversation', user_profile.user, user_profile_id.id)
    else:
        Message.objects.create(user=request.user, sender=request.user, recipient=user_profile.user, is_read=True)
        Message.objects.create(user=user_profile.user, sender=request.user, recipient=user_profile.user, is_read=True)
        # get the last user message to redirect to conversations page with him
        user_profile_id = Message.objects.filter(user=user_profile.user).latest('user')
        return redirect('conversation', user_profile.user, user_profile_id.id)

def check_message(request):
    directs_count = 0
    if request.user.is_authenticated:
        # filter with user and recipient because see who send you a message for counting.
        directs_count = Message.objects.filter(user=request.user, recipient=request.user, is_read=False).count()
    return {'directs_count': directs_count}
