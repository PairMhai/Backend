# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20170928_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='ccv',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='credit_no',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditcards', to='membership.Customer'),
        ),
    ]
