from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from accounts.models import UserProfile, Experience_user, Tags
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm, ExperienceUserForm, TagsUserForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        all_user_profile = UserProfile.objects.all()
    else:
        return redirect('home')

    context = {
        'user_profile': user_profile,
        'all_user_profile': all_user_profile
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def user_profile(request, slug_user):
    print('\nslug_user = ', slug_user)
    print('request.user = ', request.user, '\n')
    user_profile_photo = UserProfile.objects.get(user=request.user)
    user_profile = UserProfile.objects.get(user__first_name=slug_user)

    context = {
        'user_profile': user_profile,
        'user_profile_photo': user_profile_photo,
    }
    return render(request, 'profile_user/user_profile.html', context)

@login_required(login_url='login')
def edit_profile(request):
    try:
        # get userprofile
        user_profile = get_object_or_404(UserProfile, user=request.user)

        # get user_experience
        user_experience = get_object_or_404(Experience_user, experience_user=request.user)
        user_experience_form = ExperienceUserForm(instance=user_experience)

        # get user_tags
        user_tags = Tags.objects.filter(tags_user=request.user)
        user_tags_form = TagsUserForm(instance=request.user)

        if request.method == 'POST':
            # get information of userform & userprofile
            user_form = UserForm(request.POST, request.FILES, instance=request.user)
            profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

            # check user_form & profile_form is valid
            if user_form.is_valid() and profile_form.is_valid():
                # save the information updated
                user_form.save()
                profile_form.save()

                messages.success(request, 'Your profile has been updated.')
                return redirect('/accounts-setting/edit-profile/', request.user)
        else:
            user_form = UserForm(instance=request.user)
            profile_form = UserProfileForm(instance=user_profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'user_experience_form': user_experience_form,
            'user_tags_form': user_tags_form,
            'user_tags': user_tags,
            'user_profile': user_profile
        }

        return render(request, 'profile_user/edit_profile.html', context)

    except ObjectDoesNotExist:
        pass

@login_required(login_url='login')
def edit_experience_user(request):
    try:
        # get userexperience
        user_experience = get_object_or_404(Experience_user, experience_user=request.user)
        if request.method == 'POST':
            # get information of userform & userprofile
            user_experience_form = ExperienceUserForm(request.POST, request.FILES, instance=user_experience)

            # check user_form & profile_form is valid
            if user_experience_form.is_valid():

                # save the information updated
                user_experience_form.save()
                messages.success(request, 'Your profile has been updated.')
                return redirect('/accounts-setting/edit-profile/', request.user)
        else:
            user_experience_form = UserProfileForm(instance=user_experience)

        context = {
            'user_experience_form': user_experience_form,
            'user_experience': user_experience
        }

        return render(request, 'profile_user/edit_profile.html', context)

    except ObjectDoesNotExist:
        pass

@login_required(login_url='login')
def create_tags_user(request):
    try:
        # get user_profile to add new tag
        user_profile = UserProfile.objects.get(user=request.user)

        if request.method == 'POST':
            # get information of usertags
            user_tags_form = TagsUserForm(request.POST, request.FILES, instance=request.user)

            print('\nuser_tags_form.is_valid() = ', user_tags_form.is_valid(), '\n')
            # check user_form & profile_form is valid
            if user_tags_form.is_valid():
                # save the information updated
                tag = Tags.objects.create(
                    tags_user=request.user,
                    tag=user_tags_form.cleaned_data['tag']
                )
                user_profile.skills_tags.add(tag)
                tag.save()
                messages.success(request, 'your tags has been created')
                return redirect('/accounts-setting/edit-profile/', request.user)
        else:
            user_tags_form = TagsUserForm(instance=request.user)

        context = {
            'user_tags_form': user_tags_form,
        }
        return render(request, 'profile_user/edit_profile.html', context)

    except ObjectDoesNotExist:
        pass

@login_required(login_url='login')
def delete_tags_user(request, pk):
    user_profile = UserProfile.objects.get(user=request.user)
    tag = Tags.objects.get(id=pk, tags_user=user_profile.user)
    tag.delete()
    messages.success(request, 'your tag is delete')
    return redirect('/accounts-setting/edit-profile/', request.user)


def change_password(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile_user/change_password.html', context)