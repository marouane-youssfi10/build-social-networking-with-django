from django.shortcuts import render, redirect
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        # if request.user == request.user.u
        user_profile = UserProfile.objects.get(user=request.user)
        all_user_profile = UserProfile.objects.all()
    else:
        return redirect('home')
    context = {
        'user_profile': user_profile,
        'all_user_profile': all_user_profile
    }
    return render(request, 'home.html', context)

def user_profile(request):
    pass