# Generated by Django 3.1.3 on 2021-12-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20211213_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationjobs',
            old_name='text_preview',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='notificationprojects',
            name='text_preview',
        ),
        migrations.AddField(
            model_name='notificationprojects',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]