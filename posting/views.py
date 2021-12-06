from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
# models
from .models import PostProject, TagsProjects
from accounts.models import UserProfile
# forms
from .forms import PostProjectForm, TagsProjectsForm

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
            tags_list = list(tags_projects.split(',')) # separate values with commas
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
            # add tag_obj to skills tags projects
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

def search_jobs(request):
    print('------------- search jobs -------------------------')
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    print('q = ', q)
    if q == '':
        all_user_profile = UserProfile.objects.all()
        # all_user_profile = ''
    else:
        all_user_profile = UserProfile.objects.filter(
            Q(title__icontains=q) | Q(overview__icontains=q) | Q(skills_tags_user__tag__iexact=q)
        )
    print('all_user_profile = ', all_user_profile)
    context = {
        'all_user_profile': all_user_profile.distinct()
    }
    return render(request, 'pages/jobs.html', context)

def filter_jobs(request):
    all_user_profile = UserProfile.objects.all()
    if request.method == 'POST':
        if 'search_skills' in request.POST:
            search_skills = request.POST['search_skills']  # dacia
            if search_skills:
                print('search_skills = ', search_skills)
                all_user_profile = all_user_profile.filter(skills_tags_user__tag__iexact=search_skills)

        if 'availabilty' in request.POST:
            availabilty = request.POST['availabilty']
            if availabilty:
                print('availabilty = ', availabilty)
                all_user_profile = all_user_profile.filter(type_work__iexact=availabilty)

        if 'min_price' in request.POST:
            min_price = request.POST['min_price']
            max_price = request.POST['max_price']
            if max_price:
                print('min_price = ', min_price)
                print('max_price = ', max_price)
                all_user_profile = all_user_profile.filter(hourly_work__lte=max_price)
                all_user_profile = all_user_profile.filter(hourly_work__gte=min_price)

def search_projects(request):
    print('-------------search projects -------------------------')
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

        if projects.count() == 0:
            var = 'No result Found'
            return render(request, 'pages/projects.html', {'var': var})

    context = {
        'projects': projects
    }
    return render(request, 'pages/projects.html', context)

def edit_post_project(request, pk):
    # get post_project
    post_project = PostProject.objects.get(id=pk)
    if request.method == 'POST':
        # get information of post project
        post_project_form = PostProjectForm(request.POST, request.FILES, instance=post_project)

        # check user_experience_form
        if post_project_form.is_valid():
            # save the information updated
            post_project_form.save()
            messages.success(request, 'Your post has been updated')
            return redirect('projects')
    else:
        post_project_form = PostProjectForm(instance=post_project)

    context = {
        'post_project_form': post_project_form,
        'post_project': post_project
    }

    return render(request, 'post/edit_post_project.html', context)

def delete_tag_post(request, project_post_id, pk):
    tag = TagsProjects.objects.get(id=pk)
    tag.delete()
    messages.success(request, 'your tag is delete successfully')
    return redirect('/projects/edit-post/'+ str(project_post_id))

def create_tags_post(request, project_post_id):
    post_project = PostProject.objects.get(id=project_post_id)

    tags_objs = []
    for tag in post_project.skills_tags_projects.all():
        tags_objs.append(tag)

    if request.method == 'POST':
        post_tags_project = request.POST['post_tags_project']
        tags_list = list(post_tags_project.split(','))
        for tag in tags_list:
            # save the information updated
            tag, created = TagsProjects.objects.get_or_create(tags_users_projects=request.user, tag=tag)
            tags_objs.append(tag)
        post_project.skills_tags_projects.set(tags_objs)
        post_project.save()
    messages.success(request, 'your tag is created successfully')
    return redirect('/projects/edit-post/' + str(project_post_id))
