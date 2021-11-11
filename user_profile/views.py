from django.shortcuts import render
from accounts.models import UserProfile
# Create your views here.

def index(request):

    user_profile = UserProfile.objects.get(user=request.user)

    print('user_profile = ', user_profile)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'home.html', context)