# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180621_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, default=b'', max_length=254),
        ),
    ]
