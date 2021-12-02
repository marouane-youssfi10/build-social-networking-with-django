from django.shortcuts import render, redirect
from accounts.models import UserProfile
"""
if request.method == "POST":
    my_profile = Profile.objects.get(user=request.user)
    pk = request.POST.get('profile_pk')
    obj = Profile.objects.get(pk=pk)

    if obj.user in my_profile.following.all():
        my_profile.following.remove(obj.user)
    else:
        my_profile.following.add(obj.user)
    return redirect(request.META.get('HTTP_REFERER'))
return redirect('profiles:profile-list-view')
"""
def follow_unfollow_profile(request, pk):
    my_profile = UserProfile.objects.get(user=request.user)
    obj = UserProfile.objects.get(id=pk)

    if obj.user in my_profile.following.all():
        my_profile.following.remove(obj.user) # unfollow
    else:
        my_profile.following.add(obj.user) # follow

    return redirect('user-profile')