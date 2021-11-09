from django.shortcuts import render
from accounts.models import UserProfile

def home(request):
    context = {}
    return render(request, 'home.html', context)