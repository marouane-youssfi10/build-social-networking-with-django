# Generated by Django 3.2.9 on 2021-11-23 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TagsProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('tags_users_projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'tags Projects',
                'verbose_name_plural': 'TagsUsers Projects',
            },
        ),
        migrations.CreateModel(
            name='PostProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=100)),
                ('start_price', models.IntegerField()),
                ('end_price', models.IntegerField()),
                ('description_project', models.TextField()),
                ('skills_tags_projects', models.ManyToManyField(blank=True, to='posting.TagsProjects')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
