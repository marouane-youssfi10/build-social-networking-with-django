from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# models
from posting.models import PostProject
from accounts.models import UserProfile
from .models import CommentProjects, CommentJobs
# form
from .forms import CommentProjectsForm, CommentJobsForm
# Create your views here.

def comment_project(request, project_id):
    # post_project = models.ForeignKey(PostProject, related_name='post_project')
    post_project = PostProject.objects.get(id=project_id)
    comments = post_project.post_project.all()
    my_profile = UserProfile.objects.get(user=request.user)
    comments_count = comments.count()

    context = {
        'project': post_project,
        'comments': comments,
        'comments_count': comments_count,
        'my_profile': my_profile,
    }
    return render(request, 'comment/comment_post_project.html', context)

def post_comment_project(request, project_id):
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
    return redirect(reverse('comment', args=[project_id]))

def delete_comment_project(request, comment_id):
    comment_project = CommentProjects.objects.get(id=comment_id)
    comment_project.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def edit_comment_project(request, comment_id):
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

def comment_jobs(request, jobs_id):
    user_profile = UserProfile.objects.get(id=jobs_id)
    comments = user_profile.jobs_profile.all()
    my_profile = UserProfile.objects.get(user=request.user)
    comments_count = comments.count()

    print('comments = ', comments)
    context = {
        'user_profile': user_profile,
        'comments': comments,
        'comments_count': comments_count,
        'my_profile': my_profile,
    }
    return render(request, 'comment/comment_post_job.html', context)

def post_comment_jobs(request, jobs_id):
    user_profile = UserProfile.objects.get(id=jobs_id)
    if request.method == 'POST':
        comment_post_job_form = CommentJobsForm(request.POST)
        print('comment_post_job_form.is_valid(): = ', comment_post_job_form.is_valid())
        print('--------------------')
        if comment_post_job_form.is_valid():
            comment = comment_post_job_form.save(commit=False)
            comment.jobs_profile = user_profile
            comment.user_job = request.user
            comment.body = request.POST['body']
            comment.save()
    return redirect(reverse('comment-jobs', args=[jobs_id]))

def delete_comment_jobs(request, comment_id):
    comment_jobs = CommentJobs.objects.get(id=comment_id)
    comment_jobs.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def edit_comment_jobs(request, comment_id):
    comment_jobs = CommentJobs.objects.get(id=comment_id)
    jobs_id = comment_jobs.jobs_profile.id
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