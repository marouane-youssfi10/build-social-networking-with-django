from django.shortcuts import redirect

# models
from .models import Follow

def follow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)
    print('\n--------------- follow_profile ---------------')
    print('my_profile = ', my_profile_follow.user)
    print('obj        = ', obj.user, '-- obj.id = ', obj.id)

    my_profile_follow.followers.add(obj.user) # add to my_profile.followers the user who follow him
    obj.following.add(my_profile_follow.user)  # add to obj.following profile my profile

    return redirect('user-profile', obj.user, pk) # <slug:slug_user>/<int:pk>

def unfollow_profile(request, pk):
    my_profile_follow = Follow.objects.get(user=request.user)
    obj = Follow.objects.get(id=pk)
    print('\n-------------- unfollow_profile --------------')
    print('\nmy_profile = ', my_profile_follow.user)
    print('obj        = ', obj.user, '-- obj.id = ', obj.id)

    my_profile_follow.followers.remove(obj.user)
    obj.following.remove(my_profile_follow.user)

    return redirect('user-profile', obj.user, pk) # <slug:slug_user>/<int:pk>