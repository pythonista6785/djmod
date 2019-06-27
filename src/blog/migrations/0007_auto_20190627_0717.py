# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-06-27 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_postmodel_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Post Title'),
        ),
    ]
