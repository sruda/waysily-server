# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-15 23:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20170315_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='immersion',
            name='school',
        ),
        migrations.AddField(
            model_name='school',
            name='immersion',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='immersion', to='schools.Immersion'),
        ),
    ]
