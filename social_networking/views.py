from django.shortcuts import render
from accounts.models import UserProfile, Experience_user, Tags

def home(request):
    print('request.user = ', request.user)
    user_profile = UserProfile.objects.all()

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'home.html', context)
