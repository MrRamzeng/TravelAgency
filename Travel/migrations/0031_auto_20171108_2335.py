# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 23:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Travel', '0030_auto_20171108_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='sale',
            new_name='discount',
        ),
        migrations.AddField(
            model_name='allocution',
            name='username',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]