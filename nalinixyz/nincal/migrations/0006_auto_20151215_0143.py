# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nincal', '0005_auto_20151215_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]