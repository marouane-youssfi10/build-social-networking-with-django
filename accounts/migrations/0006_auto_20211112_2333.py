# Generated by Django 3.2.9 on 2021-11-12 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_hourly_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience_user',
            name='experince_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience_user',
            name='experince_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]