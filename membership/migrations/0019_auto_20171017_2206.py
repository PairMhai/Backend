# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0018_remove_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
