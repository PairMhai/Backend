# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20171004_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transportation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.Transportation'),
            preserve_default=False,
        ),
    ]