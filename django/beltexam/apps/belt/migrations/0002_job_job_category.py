# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-25 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='belt.Category'),
            preserve_default=False,
        ),
    ]
