from accounts.models import UserProfile, Account

def display_photo_profile(request):
    photo_profile_user = UserProfile.objects.get(user=request.user)
    print('--------- context_processors ---------------')
    print('photo_profile = ', photo_profile_user)
    print('--------- context_processors ---------------')
    return dict(photo_profile_user=photo_profile_user.photo_profile)

