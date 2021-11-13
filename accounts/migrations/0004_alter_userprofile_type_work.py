# Generated by Django 3.2.9 on 2021-11-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_type_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type_work',
            field=models.CharField(blank=True, choices=[('part time', 'part time'), ('full time', 'full time')], default=None, max_length=50, null=True),
        ),
    ]