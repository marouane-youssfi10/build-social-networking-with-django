from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# models
from .models import Follow
from posting.models import PostProject, PostJobs

@login_required(login_url='login')
def follow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)

    if not obj.user in my_profile_follow.following.all():
        my_profile_follow.following.add(obj.user) # add to my_profile.followers the user who follow him
        obj.followers.add(my_profile_follow.user)  # add to obj.following profile my profile

    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def unfollow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)

    if obj.user in my_profile_follow.following.all():
        my_profile_follow.following.remove(obj.user)
        obj.followers.remove(my_profile_follow.user)

    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def add_like_projects(request, pk):
    project = PostProject.objects.get(id=pk)
    if not request.user in project.likes.all():
        print('-- if not --')
        project.likes.add(request.user)
        project.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def remove_like_projects(request, pk):
    project = PostProject.objects.get(id=pk)
    if request.user in project.likes.all():
        project.likes.remove(request.user)
        project.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def add_like_jobs(request, pk):
    jobs = PostJobs.objects.get(id=pk)
    if not request.user in jobs.likes.all():
        jobs.likes.add(request.user)
        jobs.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def remove_like_jobs(request, pk):
    jobs = PostJobs.objects.get(id=pk)
    if request.user in jobs.likes.all():
        jobs.likes.remove(request.user)
        jobs.save()
    return redirect(request.META.get('HTTP_REFERER'))

