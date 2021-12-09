from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_comment(request, project_id):
    return HttpResponse('post_comment')
