# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-17 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20180617_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(),
        ),
    ]
