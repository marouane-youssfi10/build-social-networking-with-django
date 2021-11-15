from accounts.models import UserProfile
# from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def display_photo_profile(request):
    """if request.user is None:
        print('\n--------- 1:request.user = ', request.user, "\n")

    if request.user is not None:
        print('\n--------- 2:request.user = ', request.user, "\n")
        photo_profile_user = UserProfile.objects.get(user=request.user)
        return dict(photo_profile_user=photo_profile_user.photo_profile)"""
    pass

