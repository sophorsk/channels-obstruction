# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-20 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='current_turn',
        ),
    ]
