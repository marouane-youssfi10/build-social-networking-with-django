from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
# models
from accounts.models import UserProfile, Experience_user, TagsUser, Social_media
from follow.models import Follow
from posting.models import PostProject, PostJobs
# forms
from .forms import UserForm, UserProfileForm, ExperienceUserForm, TagsUserForm, SocialMediaForm
# pagination
from django.core.paginator import Paginator

@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        # get request.user for listing his info
        my_profile = UserProfile.objects.get(user=request.user)
        all_user_profile = UserProfile.objects.all()[0:5] # for "Suggestions" part in home_login page
        all_user_jobs = PostJobs.objects.all()

        # for home_login page
        paginator_project = Paginator(all_user_jobs, 3)
        page_number_projects = request.GET.get('page')
        page_all_user_jobs = paginator_project.get_page(page_number_projects)

        # get info of follow user
        follow_user = Follow.objects.get(user=request.user)

        followers_count = follow_user.following.all().count()
        following_count = follow_user.followers.all().count()
    else:
        return redirect('home')

    context = {
        'all_user_jobs': page_all_user_jobs,
        'my_profile': my_profile,
        'follow_user': follow_user,
        'following_count': following_count,
        'followers_count': followers_count,
        'all_user_profile': all_user_profile,
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def user_profile(request, name_user, pk):
    print('------------ user_profile -----------------')
    # get all user_profile for Suggestions div
    all_user_profile = UserProfile.objects.all()[0:5] # for "Suggestions" part in home_login page

    # get all experience of request.user
    user_experience = Experience_user.objects.filter(experience_user__pk=pk).exclude(experince_title=None, experince_description=None)

    # get currently user profile
    current_user_profile = UserProfile.objects.get(user__pk=pk)

    # get user_tags
    user_tags = TagsUser.objects.filter(tags_user__pk=pk)

    # get info of follow current user
    current_follow_user = Follow.objects.get(user__pk=pk)

    # get following & followers current_user
    following_count = current_follow_user.following.all().count()
    followers_count = current_follow_user.followers.all().count()

    # get all links of social networking
    links_media = Social_media.objects.filter(social_media_user=current_user_profile.user)[0:8]

    # get request user for display saved jobs
    my_profile = UserProfile.objects.get(user=request.user)

    # get request.user account Follow
    my_follow_user = Follow.objects.get(user=request.user)

    # add who see your profile
    if not my_profile.user in current_user_profile.viewers.all():
        current_user_profile.viewers.add(request.user)
        current_user_profile.save()

    context = {
        'current_user_profile': current_user_profile,
        'user_experience': user_experience,
        'user_tags': user_tags,
        'all_user_profile': all_user_profile,
        'links_media': links_media,
        'current_follow_user': current_follow_user,
        'following_count': following_count,
        'followers_count': followers_count,
        'my_profile': my_profile,
        'my_follow_user': my_follow_user
    }
    return render(request, 'profile_user/user_profile.html', context)

@login_required(login_url='login')
def edit_profile(request):

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

        # 'request_user_profile': request_user_profile
    }
    return render(request, 'profile_user/edit_profile.html', context)

@login_required(login_url='login')
def edit_experience_user(request, pk):

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
    }

    return render(request, 'profile_user/user_experience/edit_experience.html', context)

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
        'form_experience': form_experience,
    }
    return render(request, 'profile_user/user_experience/create_experience.html', context)

@login_required(login_url='login')
def delete_experience_user(request, pk):
    try:
        experience = Experience_user.objects.get(id=pk)
        experience.delete()
        messages.success(request, 'your experience is deleted')
        return redirect(reverse('/accounts-setting/edit-profile/', args=[request.user]))
    except:
        return redirect('/accounts-setting/edit-profile/', request.user)

@login_required(login_url='login')
def create_tags_user(request):
    # get user_profile to add new tag
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # get information of usertags
        user_tags_form = TagsUserForm(request.POST, request.FILES, instance=request.user)

        tags_objs = []
        if user_tags_form.is_valid():
            tags = user_tags_form.cleaned_data['tag']
            tags_list = list(tags.split(','))
            tags_list = [item.strip() for item in tags_list]  # strip all words
            while '' in tags_list: tags_list.remove('')  # remove '' from list

            # add tags to list and check if tag exists of exists.
            for tag in tags_list:
                # save the information updated
                tag, created = TagsUser.objects.get_or_create(tags_user=request.user, tag=tag)
                tags_objs.append(tag)

            # add tags to UserProfile
            user_profile.skills_tags_user.set(tags_objs)
            user_profile.save()

            if len(tags_objs) <= 1:
                messages.success(request, 'your tag has been created')
            else:
                messages.success(request, 'your tags has been created')
            return redirect('/accounts-setting/edit-profile/', request.user)
    else:
        user_tags_form = TagsUserForm(instance=request.user)

    context = {
        'user_tags_form': user_tags_form,
    }
    return render(request, 'profile_user/edit_profile.html', context)

@login_required(login_url='login')
def delete_tags_user(request, pk):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        tag = TagsUser.objects.get(id=pk, tags_user=user_profile.user)
        tag_name = tag.tag
        tag.delete()
        messages.success(request, 'your tag "' + tag_name + '" is delete')
        return redirect(reverse('/accounts-setting/edit-profile/', args=[request.user]))
    except:
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
    return render(request, 'profile_user/user_links/create_link.html', context)

@login_required(login_url='login')
def edit_links_media(request, pk):
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
    }

    return render(request, 'profile_user/user_links/edit_link.html', context)

@login_required(login_url='login')
def delete_links_media(request, pk):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        links = Social_media.objects.get(id=pk, social_media_user=user_profile.user)
        link_name = links.link
        links.delete()
        messages.success(request, 'your link "' + link_name + '" is delete')
        return redirect(reverse('/accounts-setting/edit-profile/', args=[request.user]))
    except:
        return redirect('/accounts-setting/edit-profile/', request.user)

# save jobs to my_profile
@login_required(login_url='login')
def saved_jobs(request, pk):
    # get your profile
    my_job = UserProfile.objects.get(user=request.user)

    # get the jobs you want to saved
    user_job = PostJobs.objects.get(id=pk)
    if not user_job in my_job.saved_jobs.all():
        my_job.saved_jobs.add(user_job.id)

    return redirect(request.META.get('HTTP_REFERER'))

# unsaved jobs to my_profile
@login_required(login_url='login')
def unsaved_jobs(request, pk):
    # get your profile
    my_job = UserProfile.objects.get(user=request.user)

    # get the jobs you want to unsaved
    user_job = PostJobs.objects.get(id=pk)
    if user_job in my_job.saved_jobs.all():
        my_job.saved_jobs.remove(user_job.id)

    return redirect(request.META.get('HTTP_REFERER'))

# bid a project to my_profile
@login_required(login_url='login')
def bid_project(request, pk):
    # get your profile
    my_profile = UserProfile.objects.get(user=request.user)

    # get the jobs you want to saved
    post_projects = PostProject.objects.get(id=pk)
    if not post_projects in my_profile.my_bids_projects.all():
        my_profile.my_bids_projects.add(post_projects.id)

    return redirect(request.META.get('HTTP_REFERER'))

# unbid a project to my_profile
@login_required(login_url='login')
def unbid_project(request, pk):
    # get your profile
    my_profile = UserProfile.objects.get(user=request.user)

    # get the jobs you want to saved
    post_projects = PostProject.objects.get(id=pk)
    if post_projects in my_profile.my_bids_projects.all():
        my_profile.my_bids_projects.remove(post_projects.id)

    return redirect(request.META.get('HTTP_REFERER'))

