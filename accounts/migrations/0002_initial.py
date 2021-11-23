# Generated by Django 3.2.9 on 2021-11-23 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.experience_user'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='links_media',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.social_media'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills_tags_user',
            field=models.ManyToManyField(blank=True, to='user_profile.TagsUser'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
