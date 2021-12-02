from django.shortcuts import render, redirect
from accounts.models import UserProfile
from .models import Follow

def follow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)

    print('my_profile = ', my_profile_follow)
    print('obj        = ', obj, '-- obj.id = ', obj.id)
    if obj.user in my_profile_follow.following.all():
        print('if')
        my_profile_follow.following.add(obj.user)  # follow

    # request.META.get('HTTP_REFERER')
    return redirect('/')

def unfollow_profile(request, pk):
    my_profile = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)

    print('my_profile = ', my_profile)
    print('obj        = ', obj, '-- obj.id = ', obj.id)
    if obj.user in my_profile.following.all():
        print('if')
        my_profile.following.remove(obj.user)  # unfollow

    return redirect('/')