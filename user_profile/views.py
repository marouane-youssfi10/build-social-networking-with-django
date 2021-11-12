from django.shortcuts import render, redirect
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)

    else:
        return redirect('home')
    context = {
        'user_profile': user_profile
    }
    return render(request, 'home.html', context)