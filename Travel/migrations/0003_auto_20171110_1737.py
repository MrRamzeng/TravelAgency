# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0002_auto_20171110_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour_booking',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Travel.Manager', verbose_name='\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440'),
        ),
    ]
