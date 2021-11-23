from django.shortcuts import render
from .models import PostProject, TagsProjects
# Create your views here.

def index(request):

    projects = PostProject.objects.all()

    context = {
        'projects': projects
    }
    return render(request, 'pages/projects.html', context)