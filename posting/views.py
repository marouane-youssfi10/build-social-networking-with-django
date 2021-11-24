from django.shortcuts import render
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