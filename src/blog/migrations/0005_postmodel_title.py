# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-06-27 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190627_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='New Title', max_length=30),
            preserve_default=False,
        ),
    ]