# Generated by Django 3.2.9 on 2021-12-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0013_alter_postjobs_type_work_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjobs',
            name='type_work_job',
            field=models.CharField(choices=[(1, 'Select Type Work'), ('Hourly', 'Hourly'), ('Part time', 'Part time'), ('Full time', 'Full time')], default=1, max_length=100),
        ),
    ]
