from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account, UserProfile
from user_profile.models import Experience_user, TagsUser, Social_media
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
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

            # create user into Experience_user
            experience_user = Experience_user()
            experience_user.experience_user_id = user.id
            experience_user.save()

            # create user into Social_media
            social_media = Social_media()
            social_media.social_media_user_id = user.id
            social_media.save()

            # create user into Tags
            tags = TagsUser()
            tags.tags_user_id = user.id
            tags.save()

            # create user into UserProfile
            user_profile = UserProfile.objects.create(
                user=user, slug=user.id,
                photo_profile='avatar/avatar.png',
                experience=experience_user,
                links_media=social_media,
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

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            print('\n--- if user ---', request.user, '\n')
            auth.login(request, user)
            messages.success(request, 'You are Now Logged in.')
            return redirect('index')
        else:
            print('\n--- else user ---', request.user, '\n')
            messages.error(request, 'Username Or password does not exists')

    return render(request, 'accounts/register.html')

@login_required(login_url='login')
def logoutUser(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')
