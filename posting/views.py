from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

# models
from .models import PostProject, TagsProjects
from accounts.models import UserProfile

# forms
from .forms import *

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
        form_tags_post_project = TagsProjectsForm(request.POST)

        print('form_post_projects.is_valid()     = ', form_post_project.is_valid())
        print('form_tags_post_project.is_valid() = ', form_tags_post_project.is_valid())
        tags_objs = []
        if form_post_project.is_valid() and form_tags_post_project.is_valid():
            # get the values of post_project
            name_project = form_post_project.cleaned_data['name_project']
            type_work_project = form_post_project.cleaned_data['type_work_project']
            location = form_post_project.cleaned_data['location']
            start_price = form_post_project.cleaned_data['start_price']
            end_price = form_post_project.cleaned_data['end_price']
            description_project = form_post_project.cleaned_data['description_project']

            # get the value of tags_post_values list
            tags_projects = form_tags_post_project.cleaned_data['tag']
            tags_list = list(tags_projects.split(','))
            for tag in tags_list:
                # save the information updated
                tag, created = TagsProjects.objects.get_or_create(tags_users_projects=request.user, tag=tag)
                tags_objs.append(tag)

            form_post_projects = PostProject.objects.create(
                user=request.user,
                name_project=name_project,
                type_work_project=type_work_project,
                location=location,
                start_price=start_price,
                end_price=end_price,
                description_project=description_project
            )
            form_post_projects.skills_tags_projects.set(tags_objs)
            form_post_projects.save()

            messages.success(request, 'Your Project is created')
            return redirect('/projects/')
    else:
        form_post_project = PostProjectForm()
        form_tags_post_project = TagsProjectsForm()

    context = {
        'form_post_project': form_post_project,
        'form_tags_post_project': form_tags_post_project
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
            Q(name_project__icontains=q) | Q(description_project__icontains=q) | Q(skills_tags_projects__tag__icontains=q)
        )
    context = {
        'projects': projects
    }
    return render(request, 'pages/projects.html', context)

def filter_project(request):
    projects = PostProject.objects.all()
    if request.method == 'POST':
        if 'search_skills' in request.POST:
            search_skills = request.POST['search_skills']  # dacia
            if search_skills:
                print('search_skills = ', search_skills)
                projects = projects.filter(skills_tags_projects__tag__icontains=search_skills)

        if 'availabilty' in request.POST:
            availabilty = request.POST['availabilty']
            if availabilty:
                print('availabilty = ', availabilty)
                projects = projects.filter(description_project__icontains=availabilty)

        if 'min_price' in request.POST:
            min_price = request.POST['min_price']
            max_price = request.POST['max_price']
            if max_price:
                print('min_price = ', min_price)
                print('max_price = ', max_price)
                projects = projects.filter(start_price__gte=min_price, end_price__lte=max_price)

        if 'country' in request.POST:
            country = request.POST['country']
            if country:
                print('country = ', country)
                projects = projects.filter(location__iexact=country)

        if 'experience_level' in request.POST:
            experience_level = request.POST['experience_level']
            if experience_level:
                print('experience_level = ', experience_level)
                projects = projects.filter(description_project__icontains=experience_level)
    else:
        return render(request, 'pages/projects.html')

    context = {
        'projects': projects
    }
    return render(request, 'pages/projects.html', context)
