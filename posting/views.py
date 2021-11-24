from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PostProject, TagsProjects
from accounts.models import UserProfile
from .forms import PostProjectForm
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
    print('\n post_projects \n')
    if request.method == 'POST':
        form_post_projects = PostProjectForm(request.POST)
        print('form_post_projects.is_valid() = ', form_post_projects.is_valid())
        if form_post_projects.is_valid():
            name_project = form_post_projects.cleaned_data['name_project']
            type_work_project = form_post_projects.cleaned_data['type_work_project']
            location = form_post_projects.cleaned_data['location']
            start_price = form_post_projects.cleaned_data['start_price']
            end_price = form_post_projects.cleaned_data['end_price']
            description_project = form_post_projects.cleaned_data['description_project']

            form_post_projects = PostProject.objects.create(
                user_profile=request.user,
                name_project=name_project,
                type_work_project=type_work_project,
                location=location,
                start_price=start_price,
                end_price=end_price,
                description_project=description_project,
            )
            form_post_projects.save()
            messages.success(request, 'Your Projects is created')
            print('\n if \n')
            return redirect('post-projects')
    else:
        messages.error(request, 'Your Projects is not created')
        print('\n else \n')
        return redirect('post-projects')