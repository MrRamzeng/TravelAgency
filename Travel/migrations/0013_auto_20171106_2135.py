# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0012_auto_20171106_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='comfort',
            field=models.PositiveIntegerField(verbose_name='\u041a\u043e\u043c\u0444\u043e\u0440\u0442'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='days',
            field=models.PositiveIntegerField(verbose_name='\u0414\u043d\u0435\u0439'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.PositiveIntegerField(verbose_name='\u0426\u0435\u043d\u0430'),
        ),
    ]