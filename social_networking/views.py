from django.shortcuts import render, redirect
from posting.models import PostProject
# pagination
from django.core.paginator import Paginator
def home(request):

    # check if user is authenticated
    if request.user.is_authenticated:
        return redirect('index')

    """post_projects = PostProject.objects.all()

    # for projects page
    paginator_project = Paginator(post_projects, 5)
    page_number_projects = request.GET.get('page')
    page_projects = paginator_project.get_page(page_number_projects)"""

    context = {
        'projects': 'page_projects'
    }

    return render(request, 'home.html')
