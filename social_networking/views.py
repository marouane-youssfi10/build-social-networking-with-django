from django.shortcuts import redirect, render

def home(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')

