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
    return render(request, 'profile_user/user_profile.html')


@login_required(login_url='login')
def edit_profile(request):

    userprofile = get_object_or_404(UserProfile, user=request.user)
    print('\nuserprofile = ', userprofile, '\n')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')

            context = {
                'userprofile': userprofile,
            }
            return render(request, 'edit_profile.html', context)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)


    print('\n-------------- edit_profile --------------------\n')
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }

    return render(request, 'profile_user/edit_profile.html', context)

def change_password(request):
    return render(request, 'profile_user/change_password.html')