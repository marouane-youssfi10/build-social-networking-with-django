from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import UserProfile, Experience_user, TagsUser, Social_media
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm, ExperienceUserForm, TagsUserForm, SocialMediaForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='login')
def index(request):
    # get request user for display photo in his navbar img tag
    request_user_profile = UserProfile.objects.get(user=request.user)

    # print('\n index : request.user.first_name = ', request.user.first_name, '\n')
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        all_user_profile = UserProfile.objects.all()[0:5]
    else:
        return redirect('home')

    context = {
        'user_profile': user_profile,
        'all_user_profile': all_user_profile,
        'request_user_profile': request_user_profile
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def user_profile(request, slug_user, pk):
    # get request user for display photo in his navbar img tag
    request_user_profile = UserProfile.objects.get(user=request.user)

    # get all user_profile for Suggestions div
    all_user_profile = UserProfile.objects.all()[0:5]

    # get all experience to request.user
    user_experience = Experience_user.objects.filter(experience_user=pk)

    # get currently user profile
    user_profile = UserProfile.objects.get(user__first_name=slug_user)

    # get all links of social networking
    links_media = Social_media.objects.filter(social_media_user=user_profile.user)[0:5]

    context = {
        'user_profile': user_profile,
        'request_user_profile': request_user_profile,
        'user_experience': user_experience,
        'all_user_profile': all_user_profile,
        'links_media': links_media
    }
    return render(request, 'profile_user/user_profile.html', context)

@login_required(login_url='login')
def edit_profile(request):
    try:
        # get request user for display photo in his navbar img tag
        request_user_profile = UserProfile.objects.get(user=request.user)

        # get userprofile
        user_profile = get_object_or_404(UserProfile, user=request.user)

        # get user_experience
        user_experience = Experience_user.objects.filter(experience_user=request.user)

        # get user_tags
        user_tags = TagsUser.objects.filter(tags_user=request.user)
        user_tags_form = TagsUserForm(instance=request.user)

        # get link social media
        user_links_media = Social_media.objects.filter(social_media_user=request.user)

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
            'user_tags_form': user_tags_form,

            'user_tags': user_tags,
            'user_experience': user_experience,
            'user_profile': user_profile,
            'user_links_media': user_links_media,

            'request_user_profile': request_user_profile
        }
        return render(request, 'profile_user/edit_profile.html', context)

    except ObjectDoesNotExist:
        pass

@login_required(login_url='login')
def edit_experience_user(request, pk):
    # get request user for display photo in his navbar img tag
    request_user_profile = UserProfile.objects.get(user=request.user)
    try:
        # get userexperience
        user_experience = Experience_user.objects.get(id=pk)
        if request.method == 'POST':
            print('\nif\n')
            # get information of userform & userprofile
            user_experience_form = ExperienceUserForm(request.POST, request.FILES, instance=user_experience)

            # check user_experience_form
            if user_experience_form.is_valid():
                # save the information updated
                user_experience_form.save()
                messages.success(request, 'Your profile experience has been updated')
                return redirect('/accounts-setting/edit-profile/', request.user)
        else:
            user_experience_form = ExperienceUserForm(instance=user_experience)

        context = {
            'user_experience_form': user_experience_form,
            'user_experience': user_experience,
            'request_user_profile': request_user_profile
        }

        return render(request, 'profile_user/change_experience.html', context)

    except ObjectDoesNotExist:
        pass

@login_required(login_url='login')
def create_experience_user(request):
    form_experience = ExperienceUserForm()
    if request.method == 'POST':
        form_experience = ExperienceUserForm(request.POST)
        if form_experience.is_valid():
            experince_title = form_experience.cleaned_data['experince_title']
            experince_description = form_experience.cleaned_data['experince_description']

            form_experience = Experience_user.objects.create(
                experience_user=request.user,
                experince_title=experince_title,
                experince_description=experince_description
            )
            form_experience.save()
            messages.success(request, 'Your profile experience has been updated')
            return redirect('/accounts-setting/edit-profile/', request.user)
    context = {
        'form_experience': form_experience
    }
    return render(request, 'profile_user/create_experience.html', context)

@login_required(login_url='login')
def delete_experience_user(request, pk):
    experience = Experience_user.objects.get(id=pk)
    experience.delete()
    messages.success(request, 'your experience is deleted')
    return redirect('/accounts-setting/edit-profile/', request.user)

@login_required(login_url='login')
def create_tags_user(request):
    # get user_profile to add new tag
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # get information of usertags
        user_tags_form = TagsUserForm(request.POST, request.FILES, instance=request.user)

        print('\nuser_tags_form.is_valid() = ', user_tags_form.is_valid(), '\n')
        # check user_form & profile_form is valid
        if user_tags_form.is_valid():
            # save the information updated
            tag = TagsUser.objects.create(
                tags_user=request.user,
                tag=user_tags_form.cleaned_data['tag']
            )
            tag_name = tag.tag
            user_profile.skills_tags_user.add(tag)
            tag.save()
            messages.success(request, 'your tag "'+ tag_name + '" has been created')
            return redirect('/accounts-setting/edit-profile/', request.user)
    else:
        user_tags_form = TagsUserForm(instance=request.user)

    context = {
        'user_tags_form': user_tags_form,
    }
    return render(request, 'profile_user/edit_profile.html', context)

@login_required(login_url='login')
def delete_tags_user(request, pk):
    user_profile = UserProfile.objects.get(user=request.user)
    tag = TagsUser.objects.get(id=pk, tags_user=user_profile.user)

    tag_name = tag.tag
    tag.delete()
    messages.success(request, 'your tag "' + tag_name + '" is delete')
    return redirect('/accounts-setting/edit-profile/', request.user)

@login_required(login_url='login')
def create_links_media(request):
    user_links_media = SocialMediaForm()
    if request.method == 'POST':
        # get information of links_of_social_media
        social_media_form = SocialMediaForm(request.POST)

        # check user_form & profile_form is valid
        if social_media_form.is_valid():
            name = social_media_form.cleaned_data['name']
            link = social_media_form.cleaned_data['link']

            # save the information updated
            link = Social_media.objects.create(
                social_media_user=request.user,
                name=name, link=link
            )
            # link_name = link.name
            link.save()
            # messages.success(request, 'your link "' + link_name + '" has been created')
            messages.success(request, 'your link has been created')
            return redirect('/accounts-setting/edit-profile/', request.user)

    context = {
        'user_links_media': user_links_media,
    }
    return render(request, 'profile_user/create_link.html', context)

@login_required(login_url='login')
def edit_links_media(request, pk):
    # get request user for display photo in his navbar img tag
    request_user_profile = UserProfile.objects.get(user=request.user)

    # get link of your social network or your website
    user_links_media = Social_media.objects.get(id=pk)
    if request.method == 'POST':
        print('\nif\n')
        # get information of userform & userprofile
        link_media_form = SocialMediaForm(request.POST, request.FILES, instance=user_links_media)

        # check user_experience_form
        if link_media_form.is_valid():
            # save the information updated
            link_media_form.save()
            messages.success(request, 'Your link has been updated')
            return redirect('/accounts-setting/edit-profile/', request.user)
    else:
        link_media_form = SocialMediaForm(instance=user_links_media)

    context = {
        'link_media_form': link_media_form,
        'user_links_media': user_links_media,
        'request_user_profile': request_user_profile
    }

    return render(request, 'profile_user/edit_link.html', context)

@login_required(login_url='login')
def delete_links_media(request, pk):
    user_profile = UserProfile.objects.get(user=request.user)
    links = Social_media.objects.get(id=pk, social_media_user=user_profile.user)

    link_name = links.link
    links.delete()
    messages.success(request, 'your link "' + link_name + '" is delete')
    return redirect('/accounts-setting/edit-profile/', request.user)

def change_password(request):
    request_user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'user_profile': user_profile,
        'request_user_profile': request_user_profile,
    }
    return render(request, 'profile_user/change_password.html', context)