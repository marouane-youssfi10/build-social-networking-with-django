# Generated by Django 3.2.9 on 2021-12-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0012_rename_type_work_project_postproject_epic_coder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjobs',
            name='type_work_job',
            field=models.CharField(choices=[('Hourly', 'Hourly'), ('Part time', 'Part time'), ('Full time', 'Full time')], default=None, max_length=100),
        ),
    ]