# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-29 17:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Travel.City', verbose_name='Населенный пункт'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\+7\\s[(]{1}[0-9]{3}[)]{1}\\s[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{2}$')], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='phone',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\+7\\s[(]{1}[0-9]{3}[)]{1}\\s[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{2}$')], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='tourbooking',
            name='phone',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\+7\\s[(]{1}[0-9]{3}[)]{1}\\s[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{2}$')], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='phone',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\+7\\s[(]{1}[0-9]{3}[)]{1}\\s[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{2}$')], verbose_name='Телефон'),
        ),
    ]