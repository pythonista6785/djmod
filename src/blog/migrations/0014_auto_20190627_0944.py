# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-06-27 13:44
from __future__ import unicode_literals

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190627_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author_email',
            field=models.EmailField(blank=True, max_length=240, null=True, validators=[blog.validators.validate_author_email]),
        ),
    ]