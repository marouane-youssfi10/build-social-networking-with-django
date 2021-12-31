from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# models
from user_profile.models import Experience_user, TagsUser, Social_media
from posting.models import PostProject, PostJobs
import datetime

class MyAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User mast have an email address')
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(blank=True, null=True, max_length=14)
    photo_profile = models.ImageField(upload_to='userprofile/%Y/%m/%d', default="avatar/avatar_ixe80o.png", null=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.first_name if self.first_name else ''

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True



def year_choices():
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    return YEAR_CHOICES

class UserProfile(models.Model):
    STATUS_CHOICES = (
        ('Hourly', 'Hourly'),
        ('Part time', 'Part time'),
        ('Full time', 'Full time'),
    )

    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='user_profile')
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(blank=True, max_length=100)
    overview = models.TextField(blank=True)
    photo_cover = models.ImageField(null=True, upload_to='cover/%Y/%m/%d', blank=True, default="avatar/cover_kgtasa.jpg")
    education_title = models.CharField(blank=True, max_length=100)
    education_year_start = models.IntegerField('year', choices=year_choices(), blank=True, null=True)
    education_year_end = models.IntegerField('year', choices=year_choices(), blank=True, null=True)
    education_description = models.TextField(blank=True, null=True)
    location_country = models.CharField(blank=True, max_length=100)
    location_city = models.CharField(blank=True, max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    skills_tags_user = models.ManyToManyField(TagsUser, blank=True, related_name='skills_tags_user')
    links_media = models.ForeignKey(Social_media, on_delete=models.CASCADE, blank=True, related_name='links_media')
    experience = models.ForeignKey(Experience_user, on_delete=models.CASCADE, blank=True, related_name='exp_user')
    likes = models.ManyToManyField(Account, blank=True, related_name='likes_jobs')
    saved_jobs = models.ManyToManyField(PostJobs, blank=True, related_name='saved_jobs')
    my_bids_projects = models.ManyToManyField(PostProject,  blank=True)
    viewers = models.ManyToManyField(Account, blank=True, related_name='viewers_profile')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user.first_name

    def full_year(self):
        return f'{self.education_year_start} - {self.education_year_end}'
