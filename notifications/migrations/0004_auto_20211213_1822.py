# Generated by Django 3.1.3 on 2021-12-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20211213_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationjobs',
            name='text_preview',
            field=models.TextField(blank=True),
        ),
    ]