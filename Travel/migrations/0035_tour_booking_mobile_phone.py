# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0034_auto_20171109_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour_booking',
            name='mobile_phone',
            field=models.CharField(default=1, max_length=50, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'),
            preserve_default=False,
        ),
    ]
