# Generated by Django 3.2.9 on 2021-12-23 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0011_auto_20211222_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postproject',
            old_name='type_work_project',
            new_name='epic_coder',
        ),
    ]