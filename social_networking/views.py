from django.shortcuts import render, redirect
from accounts.models import UserProfile


def home(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        return redirect('index') # index page it's home_login.html



    # display all user to home_not_login page
    user_profile = UserProfile.objects.all()

    context = {
        'user_profile': user_profile
    }
    return render(request, 'home.html', context)
