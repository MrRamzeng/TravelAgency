# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0013_auto_20171106_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocution',
            name='patronymic',
            field=models.CharField(max_length=50, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='comfort',
            field=models.IntegerField(verbose_name='\u041a\u043e\u043c\u0444\u043e\u0440\u0442'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='days',
            field=models.IntegerField(verbose_name='\u0414\u043d\u0435\u0439'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.IntegerField(verbose_name='\u0426\u0435\u043d\u0430'),
        ),
    ]