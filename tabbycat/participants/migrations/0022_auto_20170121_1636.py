# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0021_auto_20170117_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='participants.Region'),
        ),
    ]