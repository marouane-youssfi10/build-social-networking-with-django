# Generated by Django 3.2.9 on 2021-12-23 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_userprofile_viewers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-created']},
        ),
    ]