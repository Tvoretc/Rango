# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2019-04-19 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190409_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='views',
        ),
    ]
