# Generated by Django 3.2.9 on 2021-12-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0010_remove_postjobs_saved_jobs'),
        ('accounts', '0013_remove_userprofile_saved_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='saved_jobs',
            field=models.ManyToManyField(blank=True, related_name='saved_jobs', to='posting.PostJobs'),
        ),
    ]