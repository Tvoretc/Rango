# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2019-04-09 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=111),
            preserve_default=False,
        ),
    ]