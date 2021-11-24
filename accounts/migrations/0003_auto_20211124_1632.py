# Generated by Django 3.2.9 on 2021-11-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='photo_profile',
        ),
        migrations.AddField(
            model_name='account',
            name='photo_profile',
            field=models.ImageField(default='avatar/avatar.png', null=True, upload_to='userprofile/%Y/%m/%d'),
        ),
    ]
