# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0036_auto_20171109_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour_booking',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Travel.Manager', verbose_name='\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440'),
        ),
        migrations.AlterField(
            model_name='tour_booking',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Travel.Tour', verbose_name='\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0442\u0443\u0440'),
        ),
        migrations.AlterField(
            model_name='tour_booking',
            name='tourist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Travel.Tourist', verbose_name='\u0422\u0443\u0440\u0438\u0441\u0442'),
        ),
    ]