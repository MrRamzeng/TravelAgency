# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0029_auto_20171107_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour_booking',
            name='first_name',
            field=models.CharField(default='a', max_length=50, verbose_name='\u0418\u043c\u044f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour_booking',
            name='last_name',
            field=models.CharField(default='a', max_length=50, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour_booking',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='tour_booking',
            name='tourist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Travel.Tourist', verbose_name='\u0422\u0443\u0440\u0438\u0441\u0442'),
        ),
    ]