# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_auto_20170914_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='classes',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='user',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]