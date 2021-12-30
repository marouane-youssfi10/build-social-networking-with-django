from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# models
from posting.models import PostProject, PostJobs
from accounts.models import UserProfile, Account
from .models import CommentProjects, CommentJobs
# form
from .forms import CommentProjectsForm, CommentJobsForm


# ----------------------- project ----------------------------
@login_required(login_url='login')
def comment_project(request, project_id):
    # get project post and their comments
    post_project = PostProject.objects.get(id=project_id)
    comments = post_project.post_project_comment.all()
    comments_count = comments.count()

    # check if the user see this post project
    if not request.user in post_project.viewers_project.all():
        post_project.viewers_project.add(request.user)

    # count viewers_project on this post
    count_viewers_project = post_project.viewers_project.all().count()
    my_profile = UserProfile.objects.get(user=request.user)

    context = {
        'project': post_project,
        'comments': comments,
        'comments_count': comments_count,
        'my_profile': my_profile,
        'count_viewers_project': count_viewers_project,
    }
    return render(request, 'comment/comment_post_project.html', context)

@login_required(login_url='login')
def post_comment_project(request, project_id):
    try:
        post_project = PostProject.objects.get(id=project_id)
        if request.method == 'POST':
            comment_post_project_form = CommentProjectsForm(request.POST)
            print('comment_post_project_form.is_valid(): = ', comment_post_project_form.is_valid())
            print('--------------------')
            if comment_post_project_form.is_valid():
                comment = comment_post_project_form.save(commit=False)
                comment.post_project = post_project
                comment.user_post = request.user
                comment.body = request.POST['body']
                comment.save()
        return redirect(reverse('comment-projects', args=[project_id]))
    except:
        return redirect(reverse('comment-projects', args=[project_id]))

@login_required(login_url='login')
def delete_comment_project(request, comment_id):
    try:
        comment_project = CommentProjects.objects.get(id=comment_id)
        comment_project.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    except:
        return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def edit_comment_project(request, comment_id):
    try:
        comment_project = CommentProjects.objects.get(id=comment_id)
        project_id = comment_project.post_project.id

        if request.method == 'POST':
            comment_project_form = CommentProjectsForm(request.POST, request.FILES, instance=comment_project)
            if comment_project_form.is_valid():
                comment_project_form.save()
                return redirect('post-comment-project', project_id)
        else:
            comment_project_form = CommentProjectsForm(instance=comment_project)

        context = {
            'comment_project_form': comment_project_form,
            'comment_project': comment_project,
        }
        return render(request, 'comment/edit_comment.html', context)

    except:
        return redirect(request.META.get('HTTP_REFERER'))


# ----------------------- end project ------------------------

# ----------------------- jobs ------------------------
@login_required(login_url='login')
def comment_jobs(request, jobs_id):
    # get job post and their comments
    user_profile_job = PostJobs.objects.get(id=jobs_id)
    comments = user_profile_job.post_job_comment.all()
    comments_count = comments.count()  # count comments

    # check if the user see this post job
    if not request.user in user_profile_job.viewers_job.all():
        user_profile_job.viewers_job.add(request.user)

    # count viewers_job on this post
    count_viewers_job= user_profile_job.viewers_job.all().count()
    my_profile = UserProfile.objects.get(user=request.user)

    context = {
        'user_profile_job': user_profile_job,
        'my_profile': my_profile,
        'comments': comments,
        'comments_count': comments_count,
        'count_viewers_job': count_viewers_job,
    }
    return render(request, 'comment/comment_post_job.html', context)

@login_required(login_url='login')
def post_comment_jobs(request, jobs_id):
    try:
        post_job = PostJobs.objects.get(id=jobs_id)
        if request.method == 'POST':
            comment_post_job_form = CommentJobsForm(request.POST)
            print('comment_post_job_form.is_valid(): = ', comment_post_job_form.is_valid())
            print('--------------------')
            if comment_post_job_form.is_valid():
                comment = comment_post_job_form.save(commit=False)
                comment.post_job = post_job
                comment.user_job = request.user
                comment.body = request.POST['body']
                comment.save()
        return redirect(reverse('comment-jobs', args=[jobs_id]))
    except:
        return redirect(reverse('comment-jobs', args=[jobs_id]))

@login_required(login_url='login')
def delete_comment_jobs(request, comment_id):
    try:
        comment_jobs = CommentJobs.objects.get(id=comment_id)
        comment_jobs.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    except:
        return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def edit_comment_jobs(request, comment_id):
    try:
        comment_jobs = CommentJobs.objects.get(id=comment_id)
        jobs_id = comment_jobs.post_job.id
        if request.method == 'POST':
            comment_jobs_form = CommentJobsForm(request.POST, request.FILES, instance=comment_jobs)
            if comment_jobs_form.is_valid():
                comment_jobs_form.save()
                return redirect('post-comment-jobs', jobs_id)
        else:
            comment_jobs_form = CommentJobsForm(instance=comment_jobs)
        context = {
            'comment_jobs_form': comment_jobs_form,
            'comment_jobs': comment_jobs,
        }
        return render(request, 'comment/edit_comment_jobs.html', context)
    except:
        return redirect(request.META.get('HTTP_REFERER'))

# ----------------------- end jobs ------------------------
