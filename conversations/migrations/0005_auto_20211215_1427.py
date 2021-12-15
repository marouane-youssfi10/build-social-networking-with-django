# Generated by Django 3.2.9 on 2021-12-15 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversations', '0004_auto_20211215_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='im_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='me', to='accounts.account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='user_message', to=settings.AUTH_USER_MODEL),
        ),
    ]