# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 20:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0004_auto_20171105_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='price',
        ),
    ]