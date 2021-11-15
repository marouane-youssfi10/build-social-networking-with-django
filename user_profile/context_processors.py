from accounts.models import UserProfile, Account

def display_photo_profile(request):
    photo_profile_user = UserProfile.objects.get(user=request.user)
    return dict(photo_profile_user=photo_profile_user.photo_profile)

