# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0021_auto_20171107_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='hotel',
        ),
        migrations.AddField(
            model_name='tour',
            name='hotel',
            field=models.ManyToManyField(blank=True, null=True, to='Travel.Hotel', verbose_name='\u041e\u0442\u0435\u043b\u044c'),
        ),
    ]