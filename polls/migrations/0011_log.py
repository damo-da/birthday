# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20180621_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.CharField(max_length=200)),
                ('long', models.TextField()),
                ('log_level', models.IntegerField()),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
