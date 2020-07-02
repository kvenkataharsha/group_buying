# Generated by Django 3.0.1 on 2020-07-01 12:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_auto_20200701_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
