# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-06-27 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190627_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
