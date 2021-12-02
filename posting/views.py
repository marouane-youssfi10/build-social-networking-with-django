from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

# models
from .models import PostProject, TagsProjects
from accounts.models import UserProfile

# forms
from .forms import PostProjectForm

def index(request):
    print('-------------index -------------------------')
    # get all user who posting projects
    projects = PostProject.objects.all()
    all_user_profile = UserProfile.objects.all()

    context = {
        'projects': projects,
        'all_user_profile': all_user_profile,
    }
    return render(request, 'pages/projects.html', context)

def post_projects(request):
    if request.method == 'POST':
        form_post_project = PostProjectForm(request.POST)
        print('form_post_projects.is_valid() = ', form_post_project.is_valid())
        if form_post_project.is_valid():
            name_project = form_post_project.cleaned_data['name_project']
            type_work_project = form_post_project.cleaned_data['type_work_project']
            location = form_post_project.cleaned_data['location']
            start_price = form_post_project.cleaned_data['start_price']
            end_price = form_post_project.cleaned_data['end_price']
            description_project = form_post_project.cleaned_data['description_project']

            form_post_projects = PostProject.objects.create(
                user=request.user,
                name_project=name_project,
                type_work_project=type_work_project,
                location=location,
                start_price=start_price,
                end_price=end_price,
                description_project=description_project,
            )
            form_post_projects.save()
            messages.success(request, 'Your Project is created')
            print('\n if \n')
            return redirect('/projects/')
    else:
        form_post_project = PostProjectForm()

    context = {
        'form_post_project': form_post_project
    }
    return render(request, 'post/post_project.html', context)

def post_job(request):
    all_user_profile = UserProfile.objects.all()

    context = {
        'all_user_profile': all_user_profile,
    }
    return render(request, 'pages/jobs.html', context)

def search(request):
    print('-------------search -------------------------')
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    if q =='':
        projects = PostProject.objects.all()
    else:
        projects = PostProject.objects.filter(
            Q(name_project__icontains=q) | Q(skills_tags_projects__tag__icontains=q)
        )
    context = {
        'projects': projects
    }
    return render(request, 'pages/projects.html', context)