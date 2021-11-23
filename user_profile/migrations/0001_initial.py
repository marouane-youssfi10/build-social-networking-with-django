# Generated by Django 3.2.9 on 2021-11-23 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TagsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('tags_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tagUsers',
            },
        ),
        migrations.CreateModel(
            name='Social_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('facebook', 'facebook'), ('linkedin', 'linkedin'), ('instagram', 'instagram'), ('youtube', 'youtube'), ('twitter', 'twitter')], default=None, max_length=100, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('social_media_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'links media',
            },
        ),
        migrations.CreateModel(
            name='Experience_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experince_title', models.CharField(blank=True, max_length=100, null=True)),
                ('experince_description', models.TextField(blank=True, null=True)),
                ('experience_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
