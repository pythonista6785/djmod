# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-06-27 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190627_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='Post Title'),
        ),
    ]
