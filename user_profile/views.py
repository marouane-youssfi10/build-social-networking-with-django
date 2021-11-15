from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        print('\n-------------------- if --------------------')
        user_profile = UserProfile.objects.get(user=request.user)
        all_user_profile = UserProfile.objects.all()
    else:
        print('\n------------------- else -------------------')
        return redirect('home')

    print('\n-----------------------------------------------------------------------')
    print('user_profile ', user_profile)
    print('all_user_profile = ', all_user_profile)
    print('\n-----------------------------------------------------------------------')

    context = {
        'user_profile': user_profile,
        'all_user_profile': all_user_profile
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile_user/user_profile.html', context)


@login_required(login_url='login')
def edit_profile(request):

    user_profile = get_object_or_404(UserProfile, user=request.user)
    print('\nuserprofile = ', user_profile, '\n')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')

            context = {
                'userprofile': user_profile,
            }
            return render(request, 'edit_profile.html', context)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    print('\n-------------- edit_profile --------------------\n')
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile': user_profile,
    }

    return render(request, 'profile_user/edit_profile.html', context)

def change_password(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile_user/change_password.html', context)