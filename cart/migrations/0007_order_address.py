# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20171022_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=0, max_length=150),
        ),
    ]
