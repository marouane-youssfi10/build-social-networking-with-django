from django.shortcuts import redirect

# models
from .models import Follow
from posting.models import PostProject
from accounts.models import UserProfile

def follow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)
    print('\n--------------- follow_profile ---------------')
    print('my_profile = ', my_profile_follow.user)
    print('obj        = ', obj.user, '-- obj.id = ', obj.id)

    my_profile_follow.following.add(obj.user) # add to my_profile.followers the user who follow him
    obj.followers.add(my_profile_follow.user)  # add to obj.following profile my profile

    return redirect(request.META.get('HTTP_REFERER'))

def unfollow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)
    print('\n-------------- unfollow_profile --------------')
    print('\nmy_profile = ', my_profile_follow.user)
    print('obj        = ', obj.user, '-- obj.id = ', obj.id)

    my_profile_follow.following.remove(obj.user)
    obj.followers.remove(my_profile_follow.user)

    return redirect(request.META.get('HTTP_REFERER'))

def add_like_projects(request, pk):
    project = PostProject.objects.get(id=pk)
    project.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

def remove_like_projects(request, pk):
    project = PostProject.objects.get(id=pk)
    project.likes.remove(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

def add_like_jobs(request, pk):
    print('request = ', request)
    user_profile = UserProfile.objects.get(id=pk)
    user_profile.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

def remove_like_jobs(request, pk):
    print('request = ', request)
    user_profile = UserProfile.objects.get(id=pk)
    user_profile.likes.remove(request.user)
    return redirect(request.META.get('HTTP_REFERER'))
