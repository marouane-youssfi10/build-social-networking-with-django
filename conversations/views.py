from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
from accounts.models import Account
from django.db.models import Max, Min, Count
from django.db.models import Subquery, OuterRef, F
def inbox(request):
    # get all message of users  who send message
    messages_users = Message.objects.filter(recipient=request.user).exclude(user=request.user)
    test0 = Message.objects.all().exclude(user=request.user)
    print('test0 = ', test0, '\n')

    # messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
    test0_updated = test0.values('user', 'body').annotate(latest_date=Max('updated')).order_by('-updated')
    print('test0_updated = ', test0_updated)
    for i in test0_updated:
        print(i)
    print()
    context = {
        'messages_users': messages_users
    }
    return render(request, 'conversations/messages.html', context)

def conversations(request, recipient_id):

    to_user = Message.objects.get(id=recipient_id)
    messages_users = Message.objects.filter(recipient=request.user).exclude(user=request.user)

    conversations = Message.objects.filter(user=request.user)
    conversations = conversations.filter(sender=request.user, recipient=to_user.user) | conversations.filter(sender=to_user.user, recipient=request.user)

    context = {
        'messages_users': messages_users,
        'conversations': conversations,
        'to_user': to_user,
    }
    return render(request, 'conversations/messages.html', context)