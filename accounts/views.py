from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account, UserProfile, Experience_user
from django.contrib import messages, auth
# Create your views here.


def registerPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # using clean data for fetch the value from the request
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            # create user
            user = Account.objects.create_user(first_name=first_name, last_name=last_name,
                                               email=email, username=username, password=password)
            user.phone_number = phone_number

            # create user in user_profile & experience_user
            user_profile = UserProfile.objects.create(user=user)
            experience_user = Experience_user.objects.create(experience_user=user)

            # save the user into accounts & experience_user & user_profile
            user.save()
            user_profile.save()
            experience_user.save()
            messages.success(request, 'Congratulations! Your account is activated.')
            return redirect('login')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def loginPage(request):

    # check user is is_authenticated
    if request.user.is_authenticated:
        return redirect('index')


    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are Now Logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Username Or password does not exists')

    return render(request, 'accounts/register.html')

def logoutUser(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')
