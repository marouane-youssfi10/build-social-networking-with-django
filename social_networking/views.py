from django.shortcuts import render, redirect

def home(request):

    # check if user is authenticated
    if request.user.is_authenticated:
        return redirect('index')

    return render(request, 'accounts/login.html')
