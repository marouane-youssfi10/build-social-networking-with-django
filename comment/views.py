from django.shortcuts import render
from django.http import HttpResponse
# models
from posting.models import PostProject
from accounts.models import UserProfile
# Create your views here.

def comment(request, project_id):
    # post_project = models.ForeignKey(PostProject, related_name='post_project')

    post_project = PostProject.objects.get(id=project_id)
    comment = post_project.post_project.all()
    print('post_project = ', post_project)
    print('comment =', comment)
    context = {
        'project': post_project
    }
    return render(request, 'comment/comment_post_project.html', context)

def post_comment(request, project_id):
    return HttpResponse('post_comment')
