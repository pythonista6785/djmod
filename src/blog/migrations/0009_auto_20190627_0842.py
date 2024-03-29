# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-06-27 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_postmodel_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
