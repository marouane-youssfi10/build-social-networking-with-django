# Generated by Django 3.2.9 on 2021-12-25 11:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20211225_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]