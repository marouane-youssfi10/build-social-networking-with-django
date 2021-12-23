from django.shortcuts import redirect
# models
from .models import Follow
from posting.models import PostProject, PostJobs

def follow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)

    my_profile_follow.following.add(obj.user) # add to my_profile.followers the user who follow him
    obj.followers.add(my_profile_follow.user)  # add to obj.following profile my profile

    return redirect(request.META.get('HTTP_REFERER'))

def unfollow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)

    my_profile_follow.following.remove(obj.user)
    obj.followers.remove(my_profile_follow.user)

    return redirect(request.META.get('HTTP_REFERER'))

def add_like_projects(request, pk):
    project = PostProject.objects.get(id=pk)
    project.likes.add(request.user)
    project.save()
    return redirect(request.META.get('HTTP_REFERER'))

def remove_like_projects(request, pk):
    project = PostProject.objects.get(id=pk)
    project.likes.remove(request.user)
    project.save()
    return redirect(request.META.get('HTTP_REFERER'))

def add_like_jobs(request, pk):
    jobs = PostJobs.objects.get(id=pk)
    jobs.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

def remove_like_jobs(request, pk):
    jobs = PostJobs.objects.get(id=pk)
    jobs.likes.remove(request.user)
    return redirect(request.META.get('HTTP_REFERER'))
