from django.shortcuts import render, redirect
from accounts.models import UserProfile

def home(request):
    user_profile = UserProfile.objects.all()

    context = {
        'user_profile': user_profile,
    }

    if request.user.is_authenticated:
        print('\n------------- request.user.is_authenticated index -------------\n')
        return render(request, 'index.html', context)

    return render(request, 'home.html', context)
