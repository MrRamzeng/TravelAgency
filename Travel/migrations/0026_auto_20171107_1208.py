# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0025_auto_20171107_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='tour_price',
            field=models.PositiveSmallIntegerField(default=12000, verbose_name='\u0426\u0435\u043d\u0430'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='tour_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Travel.Tour', verbose_name='\u0426\u0435\u043d\u0430 \u0442\u0443\u0440\u0430'),
        ),
    ]