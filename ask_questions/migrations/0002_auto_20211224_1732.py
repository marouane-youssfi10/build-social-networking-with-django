# Generated by Django 3.2.9 on 2021-12-24 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ask_questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask_questions',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_ask', to='accounts.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tagsquestions',
            name='tags_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
            preserve_default=False,
        ),
    ]
