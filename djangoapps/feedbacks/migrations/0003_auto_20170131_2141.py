# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_feedback_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='uid',
            field=models.CharField(max_length=200),
        ),
    ]
