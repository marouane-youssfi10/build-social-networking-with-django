from django.shortcuts import render, redirect
from accounts.models import UserProfile
from accounts.forms import RegistrationForm

def home(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        return redirect('index') # index page it's home_login.html

    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
