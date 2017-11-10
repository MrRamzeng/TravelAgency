# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 17:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='username',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tourist',
            name='username',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
            preserve_default=False,
        ),
    ]