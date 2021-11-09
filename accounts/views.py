from django.shortcuts import render

# Create your views here.


def registerPage(request):
    return render(request, 'accounts/register.html')

def loginPage(request):
    return render(request, 'accounts/login_register.html')

def logoutUser(request):
    return render(request, 'accounts/logout.html')