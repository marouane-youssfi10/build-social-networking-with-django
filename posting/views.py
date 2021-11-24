from django.shortcuts import render, redirect
from .models import PostProject, TagsProjects
from accounts.models import UserProfile
# Create your views here.

def index(request):

    # get all user who posting projects
    projects = PostProject.objects.all()

    # get request user for display photo in his navbar img tag
    request_user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'projects': projects,

        'request_user_profile': request_user_profile
    }
    return render(request, 'pages/projects.html', context)

def post_projects(request):
    """# get request user for display photo in his navbar img tag
    request_user_profile = UserProfile.objects.get(user=request.user)
    form_experience = ExperienceUserForm()
    if request.method == 'POST':
        form_experience = ExperienceUserForm(request.POST)
        if form_experience.is_valid():
            experince_title = form_experience.cleaned_data['experince_title']
            experince_description = form_experience.cleaned_data['experince_description']

            form_experience = Experience_user.objects.create(  experience_user=request.user )
            form_experience.save()
            messages.success(request, 'Your profile experience has been updated')
            return redirect('/accounts-setting/edit-profile/', request.user)
    context = { 'form_experience': form_experience, 'request_user_profile': request_user_profile }
    return render(request, 'profile_user/create_experience.html', context)"""
    return redirect('index')