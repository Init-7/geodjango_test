# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-29 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('est', '0012_auto_20160621_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='last_z',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
