# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='article',
            field=models.CharField(choices=[(b'a', b'a'), (b'an', b'an'), (b'the', b'the')], max_length=3),
        ),
    ]
