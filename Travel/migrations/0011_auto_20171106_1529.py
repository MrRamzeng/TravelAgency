# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0010_auto_20171106_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allocution',
            old_name='patronymic',
            new_name='patronym',
        ),
        migrations.AlterField(
            model_name='allocution',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='\u0418\u043c\u044f'),
        ),
    ]