# Generated by Django 3.2.9 on 2021-12-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0003_auto_20211213_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
