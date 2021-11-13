from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account, UserProfile, Experience_user, Tags
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

            # create user and save the information user
            user = Account.objects.create_user(first_name=first_name, last_name=last_name,
                                               email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            print('\nuser = ', user, '\n')
            # create user into Experience_user
            experience_user = Experience_user()
            experience_user.experience_user_id = user.id
            experience_user.save()

            # create user into Tags
            tags = Tags()
            tags.user_tags_id = user.id
            tags.save()

            # create user into UserProfile
            user_profile = UserProfile.objects.create(
                user=user, photo_profile='avatar/avatar.png',
                experience=experience_user
                    )
            user_profile.save()


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
