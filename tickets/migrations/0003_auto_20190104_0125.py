# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-04 01:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20190104_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='feature',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.Features'),
        ),
    ]