# Generated by Django 3.2.9 on 2021-11-23 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0002_postproject_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='postproject',
            name='type_work_project',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]