# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-06-27 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190627_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='publish',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('private', 'Private')], default='draft', max_length=120),
        ),
    ]
