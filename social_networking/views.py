from django.shortcuts import render
from accounts.models import UserProfile


def home(request):
    user_profile = UserProfile.objects.all()

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'home.html', context)
