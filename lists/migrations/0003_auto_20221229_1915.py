# Generated by Django 2.2.5 on 2022-12-29 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20221209_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.OneToOneField(default=uuid.uuid1, on_delete=django.db.models.deletion.CASCADE, related_name='list', to=settings.AUTH_USER_MODEL),
        ),
    ]
