# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0009_auto_20171106_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocution',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='allocution',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
    ]