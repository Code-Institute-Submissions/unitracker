# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 12:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0003_auto_20180527_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservotes',
            name='user',
        ),
        migrations.AddField(
            model_name='uservotes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
