# Generated by Django 3.2.9 on 2021-11-09 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experience_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experince_title', models.CharField(max_length=100)),
                ('experince_description', models.CharField(blank=True, max_length=100)),
                ('experince_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.TextField(blank=True)),
                ('photo_profile', models.ImageField(default='avatar/avatar.jpg', null=True, upload_to='userprofile/%Y/%m/%d')),
                ('education_title', models.CharField(blank=True, max_length=100)),
                ('education_year_start', models.IntegerField()),
                ('education_year_end', models.IntegerField()),
                ('education_description', models.TextField(blank=True)),
                ('location_country', models.CharField(blank=True, max_length=100)),
                ('location_city', models.CharField(blank=True, max_length=100)),
                ('hourly_work', models.IntegerField(blank=True)),
                ('type_work', models.CharField(blank=True, choices=[('part time', 'part time'), ('full time', 'full time')], max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.experience_user')),
                ('skills_tags', models.ManyToManyField(blank=True, to='accounts.Tags')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
