from django.shortcuts import render, redirect
from accounts.models import UserProfile


def home(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        return redirect('index')

    user_profile = UserProfile.objects.all()

    print('\nuser_profile = ', user_profile, '\n')

    print(request.user)
    if request.user.is_authenticated:
        print('request.user.is_authenticated')
    else:
        print('request.user.is_not_authenticated -- AnonymousUser')
    print()

    context = {
        'user_profile': user_profile
    }
    return render(request, 'home.html', context)
