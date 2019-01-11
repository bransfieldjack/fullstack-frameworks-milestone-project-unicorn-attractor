# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-11 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('assigned', 'ASSIGNED'), ('in progess', 'IN PROGRESS'), ('completed', 'COMPLETED')], default='assigned', max_length=10),
        ),
        migrations.AddField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('assigned', 'ASSIGNED'), ('in progess', 'IN PROGRESS'), ('completed', 'COMPLETED')], default='assigned', max_length=10),
        ),
    ]
