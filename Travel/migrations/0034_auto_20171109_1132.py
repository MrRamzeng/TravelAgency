# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0033_auto_20171109_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour_booking',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='tour_booking',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
    ]
