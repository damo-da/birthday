# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_emailmaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
        migrations.AlterField(
            model_name='emailmaster',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
    ]
