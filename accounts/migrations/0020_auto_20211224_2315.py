# Generated by Django 3.2.9 on 2021-12-24 22:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_userprofile_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='body',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='education_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='overview',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
