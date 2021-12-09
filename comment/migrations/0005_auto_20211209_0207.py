# Generated by Django 3.2.9 on 2021-12-09 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0004_alter_postproject_options'),
        ('accounts', '0002_initial'),
        ('comment', '0004_auto_20211209_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentjobs',
            name='jobs_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_profile', to='accounts.userprofile'),
        ),
        migrations.AlterField(
            model_name='commentprojects',
            name='post_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_project', to='posting.postproject'),
        ),
    ]
