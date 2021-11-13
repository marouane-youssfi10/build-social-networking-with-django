from django.shortcuts import render, redirect
from accounts.models import UserProfile

def home(request):
    user_profile = UserProfile.objects.all()

    if request.user.is_authenticated:
        return redirect('index')
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'home.html', context)
