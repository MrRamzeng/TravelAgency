# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0011_auto_20171106_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allocution',
            old_name='patronym',
            new_name='patronymic',
        ),
    ]
