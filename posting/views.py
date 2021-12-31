from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# models
from .models import PostProject, TagsProjects, TagsJobs, PostJobs
from accounts.models import UserProfile
# forms
from .forms import PostProjectForm, TagsProjectsForm, PostJobForm, TagsJobForm
# pagination
from django.core.paginator import Paginator


@login_required(login_url='login')
def projects(request):
    print('-----------------  projects ---------------------')
    # get all user who posting projects and user profile
    projects = PostProject.objects.all()
    my_profile = UserProfile.objects.get(user=request.user)

    # for projects page
    paginator_project = Paginator(projects, 7)
    page_number_projects = request.GET.get('page')
    page_projects = paginator_project.get_page(page_number_projects)

    context = {
        'projects': page_projects,
        'my_profile': my_profile,
    }
    return render(request, 'pages/projects.html', context)

@login_required(login_url='login')
def jobs(request):
    print('-----------------  jobs ---------------------')
    # get all jobs users and my profile
    all_user_profile = PostJobs.objects.all()
    my_profile = UserProfile.objects.get(user=request.user)

    # for jobs page
    paginator_jobs = Paginator(all_user_profile, 7)
    page_number_jobs = request.GET.get('page')
    page_all_user_profile = paginator_jobs.get_page(page_number_jobs)

    context = {
        'all_user_profile': page_all_user_profile,
        'my_profile': my_profile,
    }
    return render(request, 'pages/jobs.html', context)

@login_required(login_url='login')
def search_jobs(request):
    print('------------------ search jobs ------------------')
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    all_user_profile = PostJobs.objects.filter(
            Q(name_jobs__icontains=q) | Q(description_job__icontains=q) | Q(skills_tags_jobs__tag__iexact=q)
        ).distinct()

    paginator_jobs = Paginator(all_user_profile, 7)
    page_number_jobs = request.GET.get('page')
    page_all_user_profile = paginator_jobs.get_page(page_number_jobs)

    context = {
        'all_user_profile': page_all_user_profile
    }
    return render(request, 'pages/jobs.html', context)

@login_required(login_url='login')
def filter_jobs(request):
    print('---------------------- filter jobs -------------------------')
    all_user_profile = PostJobs.objects.all()
    print('all_user_profile = ', all_user_profile)

    if request.method == 'POST':
        if 'search_skills' in request.POST:
            search_skills = request.POST['search_skills']  # dacia
            if search_skills:
                print('search_skills = ', search_skills)
                all_user_profile = all_user_profile.filter(skills_tags_jobs__tag__icontains=search_skills)

        if 'availabilty' in request.POST:
            availabilty = request.POST['availabilty']
            if availabilty:
                print('availabilty = ', availabilty)
                all_user_profile = all_user_profile.filter(type_work_job__iexact=availabilty)

        if 'min_price' in request.POST:
            min_price = request.POST['min_price']
            max_price = request.POST['max_price']
            if max_price:
                print('min_price = ', min_price)
                print('max_price = ', max_price)
                all_user_profile = all_user_profile.filter(price__gte=min_price, price__lte=max_price)

        if 'country' in request.POST:
            country = request.POST['country']
            if country:
                print('country = ', country)
                all_user_profile = all_user_profile.filter(location__iexact=country)

        if 'experience_level' in request.POST:
            experience_level = request.POST['experience_level']
            if experience_level:
                print('experience_level = ', experience_level)
                all_user_profile = all_user_profile.filter(description_job__icontains=experience_level)

    context = {
        'all_user_profile': all_user_profile,
    }
    return render(request, 'pages/jobs.html', context)

# this method for posting a project
@login_required(login_url='login')
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
            epic_coder = form_post_project.cleaned_data['epic_coder']
            location = form_post_project.cleaned_data['location']
            start_price = form_post_project.cleaned_data['start_price']
            end_price = form_post_project.cleaned_data['end_price']
            description_project = form_post_project.cleaned_data['description_project']

            # get the value of tags_post_values list
            tags_projects = form_tags_post_project.cleaned_data['tag']
            tags_list = list(tags_projects.split(',')) # separate values with commas
            tags_list = [item.strip() for item in tags_list] # strip all words
            while '' in tags_list: tags_list.remove('') # remove '' from list

            for tag in tags_list:
                # save the information updated
                tag, created = TagsProjects.objects.get_or_create(tags_users_projects=request.user, tag=tag)
                tags_objs.append(tag)

            form_post_projects = PostProject.objects.create(
                user=request.user,
                name_project=name_project,
                epic_coder=epic_coder,
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

# this method for posting a job
@login_required(login_url='login')
def post_job(request):
    if request.method == 'POST':
        form_post_job = PostJobForm(request.POST)
        form_tags_post_job = TagsJobForm(request.POST)

        print('form_post_job.is_valid()      = ', form_post_job.is_valid())
        print('form_tags_post_job.is_valid() = ', form_tags_post_job.is_valid())
        tags_objs = []
        if form_post_job.is_valid() and form_tags_post_job.is_valid():
            # get the values of post_project
            name_jobs = form_post_job.cleaned_data['name_jobs']
            type_work_job = form_post_job.cleaned_data['type_work_job']
            epic_coder = form_post_job.cleaned_data['epic_coder']
            location = form_post_job.cleaned_data['location']
            price = form_post_job.cleaned_data['price']
            description_job = form_post_job.cleaned_data['description_job']

            # get the value of tags_post_values list
            tags_jobs = form_tags_post_job.cleaned_data['tag']
            tags_list = list(tags_jobs.split(','))  # separate values with commas
            tags_list = [item.strip() for item in tags_list]  # strip all words
            while '' in tags_list: tags_list.remove('')  # remove '' from list
            for tag in tags_list:
                # save the information updated
                tag, created = TagsJobs.objects.get_or_create(tags_users_jobs=request.user, tag=tag)
                tags_objs.append(tag)

            form_post_jobs = PostJobs.objects.create(
                user=request.user,
                name_jobs=name_jobs,
                type_work_job=type_work_job,
                epic_coder=epic_coder,
                location=location,
                price=price,
                description_job=description_job
            )
            # add tag_obj to skills tags projects
            form_post_jobs.skills_tags_jobs.set(tags_objs)
            form_post_jobs.save()

            messages.success(request, 'Your Job is created')
            return redirect('/jobs/')
    else:
        form_post_job = PostJobForm()
        form_tags_post_job = TagsJobForm()

    context = {
        'form_post_job': form_post_job,
        'form_tags_post_job': form_tags_post_job
    }
    return render(request, 'post/post_job.html', context)

@login_required(login_url='login')
def search_projects(request):
    print('-------------search projects -------------------------')
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    if q =='':
        projects = PostProject.objects.all()
    else:
        projects = PostProject.objects.filter(
            Q(name_project__icontains=q) | Q(description_project__icontains=q) | Q(skills_tags_projects__tag__icontains=q)
        ).distinct()

    paginator_projects = Paginator(projects, 7)
    page_number_projects = request.GET.get('page')
    page_all_projects = paginator_projects.get_page(page_number_projects)
    context = {
        'projects': page_all_projects
    }
    return render(request, 'pages/projects.html', context)

@login_required(login_url='login')
def filter_project(request):
    print('---------------------- filter projects -------------------------')
    my_profile = UserProfile.objects.get(user=request.user)
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

    paginator_projects = Paginator(projects, 7)
    page_number_projects = request.GET.get('page')
    page_all_projects = paginator_projects.get_page(page_number_projects)
    context = {
        'projects': page_all_projects,
        'my_profile': my_profile,
    }
    return render(request, 'pages/projects.html', context)

# this method for update on post
@login_required(login_url='login')
def edit_post_project(request, pk):
    # get post_project
    post_project = PostProject.objects.get(id=pk)
    if request.method == 'POST':
        # get information of post project
        post_project_form = PostProjectForm(request.POST, request.FILES, instance=post_project)
        print('post_project_form.is_valid() = ', post_project_form.is_valid())
        # check user_experience_form
        if post_project_form.is_valid():
            # save the information updated
            post_project_form.save()
            messages.success(request, 'Your post project has been updated')
            return redirect('projects')
    else:
        post_project_form = PostProjectForm(instance=post_project)

    context = {
        'post_project_form': post_project_form,
        'post_project': post_project
    }

    return render(request, 'post/edit_post_project.html', context)

# this method for update on post
@login_required(login_url='login')
def edit_post_job(request, pk):
    # get post_project
    post_job = PostJobs.objects.get(id=pk)
    if request.method == 'POST':
        # get information of post job
        post_job_form = PostJobForm(request.POST, request.FILES, instance=post_job)

        # check user_experience_form
        if post_job_form.is_valid():
            # save the information updated
            post_job_form.save()
            messages.success(request, 'Your post job has been updated')
            return redirect('jobs')
    else:
        post_job_form = PostJobForm(instance=post_job)

    context = {
        'post_job_form': post_job_form,
        'post_job': post_job
    }
    return render(request, 'post/edit_post_job.html', context)

@login_required(login_url='login')
def delete_post_projects(request, project_id):
    print('------- delete_post_projects -------')
    try:
        post_project = PostProject.objects.get(id=project_id)
        post_project.delete()
        messages.success(request, 'your project post is delete successfully')
        return redirect(request.META.get('HTTP_REFERER'))
    except:
        return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def delete_post_jobs(request, job_id):
    print('------- delete_post_jobs -------')
    try:
        post_job = PostJobs.objects.get(id=job_id)
        post_job.delete()
        messages.success(request, 'your job post is delete successfully')
        return redirect(request.META.get('HTTP_REFERER'))
    except:
        return redirect(request.META.get('HTTP_REFERER'))

# this method for delete tags on post you want to update
@login_required(login_url='login')
def delete_tag_post_project(request, project_post_id, pk):
    try:
        tag = TagsProjects.objects.get(id=pk)
        tag.delete()
        messages.success(request, 'your tag is delete successfully')
        return redirect(reverse('/projects/edit-post/', args=[project_post_id]))
    except:
        return redirect('/projects/edit-post/'+ str(project_post_id))

@login_required(login_url='login')
def delete_tag_post_job(request, job_post_id, pk):
    try:
        tag = TagsJobs.objects.get(id=pk)
        tag.delete()
        messages.success(request, 'your tag is delete successfully')
        return redirect(reverse('/jobs/edit-post/', args=[job_post_id]))
    except:
        return redirect('/jobs/edit-post/' + str(job_post_id))

# this method for create tags on post you want to update
@login_required(login_url='login')
def create_tags_post_project(request, project_post_id):
    post_project = PostProject.objects.get(id=project_post_id)

    tags_objs = []
    for tag in post_project.skills_tags_projects.all():
        tags_objs.append(tag)

    if request.method == 'POST':
        post_tags_project = request.POST['post_tags_project']
        tags_list = list(post_tags_project.split(','))
        tags_list = [item.strip() for item in tags_list]  # strip all words
        while '' in tags_list: tags_list.remove('')  # remove '' from list

        for tag in tags_list:
            # save the information updated
            tag, created = TagsProjects.objects.get_or_create(tags_users_projects=request.user, tag=tag)
            tags_objs.append(tag)
        post_project.skills_tags_projects.set(tags_objs)
        post_project.save()
    messages.success(request, 'your tag is created successfully')
    return redirect('/projects/edit-post/' + str(project_post_id))

# this method for create tags on post you want to update
@login_required(login_url='login')
def create_tags_post_job(request, job_post_id):
    post_job = PostJobs.objects.get(id=job_post_id)

    tags_objs = []
    for tag in post_job.skills_tags_jobs.all():
        tags_objs.append(tag)

    if request.method == 'POST':
        post_tags_job = request.POST['post_tags_job']
        tags_list = list(post_tags_job.split(','))
        tags_list = [item.strip() for item in tags_list]  # strip all words
        while '' in tags_list: tags_list.remove('')  # remove '' from list

        for tag in tags_list:
            # save the information updated
            tag, created = TagsJobs.objects.get_or_create(tags_users_jobs=request.user, tag=tag)
            tags_objs.append(tag)
        post_job.skills_tags_jobs.set(tags_objs)
        post_job.save()
    messages.success(request, 'your tag is created successfully')
    return redirect('/jobs/edit-post/' + str(job_post_id))

@login_required(login_url='login')
def hide_projects(request, pk):
    post_project = PostProject.objects.get(id=pk)
    post_project.hide = True
    post_project.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def unhide_projects(request, pk):
    post_project = PostProject.objects.get(id=pk)
    post_project.hide = False
    post_project.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def hide_jobs(request, job_id):
    post_job = PostJobs.objects.get(id=job_id)
    post_job.hide = True
    post_job.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def unhide_jobs(request, job_id):
    post_job = PostJobs.objects.get(id=job_id)
    post_job.hide = False
    post_job.save()
    return redirect(request.META.get('HTTP_REFERER'))
