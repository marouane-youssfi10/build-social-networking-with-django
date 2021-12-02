from django.shortcuts import render, redirect
from accounts.models import UserProfile
from .models import Follow

def follow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)
    print('\n--------------- follow_profile ---------------')
    print('my_profile = ', my_profile_follow.user)
    print('obj        = ', obj.user, '-- obj.id = ', obj.id)

    my_profile_follow.following.add(obj.user) # add to my profile the user who following you
    obj.followers.add(my_profile_follow.user)  # add to obj profile in follower field my profile

    return redirect('/')

def unfollow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)
    print('\n-------------- unfollow_profile --------------')
    print('\nmy_profile = ', my_profile_follow.user)
    print('obj        = ', obj.user, '-- obj.id = ', obj.id)

    my_profile_follow.following.remove(obj.user)
    obj.followers.remove(my_profile_follow.user)

    return redirect('/')