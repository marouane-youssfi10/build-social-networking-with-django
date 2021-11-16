from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import UserProfile, Experience_user
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm, ExperienceUserForm
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
def edit_profile(request, pk):

    # get request user
    user_profile = get_object_or_404(UserProfile, id=pk)
    user_experience = get_object_or_404(Experience_user, id=pk)
    print('\n user_profile = ', user_profile, '--', user_profile.id, '\n')
    print('\n user_experience = ', user_experience, '--', user_experience.id, '\n')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        experience_form = ExperienceUserForm(request.POST, request.FILES, instance=user_experience)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid() and experience_form.is_valid():
            print('\nbaby\n')
            experience_form.experience_user_id = user_experience.id
            profile_form.experience.user_experience = user_experience.id

            user_form.save()
            experience_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')

            context = {
                'userprofile': user_profile,
            }
            return render(request, 'profile_user/edit_profile.html', context)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)
        experience_form = ExperienceUserForm(instance=user_experience)

    # print('\n-------------- edit_profile --------------------\n')
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'experience_form': experience_form,
        'user_profile': user_profile
    }

    return render(request, 'profile_user/edit_profile.html', context)

def change_password(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile_user/change_password.html', context)