# Generated by Django 3.2.9 on 2021-11-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]