# Generated by Django 3.2.9 on 2021-12-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20211214_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
