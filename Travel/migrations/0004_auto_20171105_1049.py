# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0003_auto_20171105_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='hotel',
        ),
        migrations.AddField(
            model_name='tour',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Travel.Hotel', verbose_name='\u041e\u0442\u0435\u043b\u044c'),
        ),
    ]