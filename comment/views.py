from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# models
from posting.models import PostProject
from accounts.models import UserProfile
from .models import CommentProjects
# form
from .forms import CommentProjectsForm, CommentJobsForm
# Create your views here.

def comment(request, project_id):
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

def delete_comment(request, comment_id):
    comment_project = CommentProjects.objects.get(id=comment_id)
    # post_project = PostProject.objects.get(id=project_id)
    comment_project.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def edit_comment(request, comment_id):
    """
    get userexperience
    user_experience = Experience_user.objects.get(id=pk)
    if request.method == 'POST':
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
    """
    comment_project = CommentProjects.objects.get(id=comment_id)
    if request.method == 'POST':
        comment_project_form = CommentProjectsForm(request.POST, request.FILES, instance=comment_project)
        if comment_project_form.is_valid():
            comment_project_form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        comment_project_form = CommentProjectsForm(instance=comment_project)

    context = {
        'comment_project_form': comment_project_form,
        'comment_project': comment_project,
    }
    return render(request, 'comment/edit_comment.html', context)

def post_comment_jobs(request, project_id):
    return HttpResponse('post_comment')
