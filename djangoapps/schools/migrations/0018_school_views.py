# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-04 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0017_school_other_language_teach'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='views',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='It is have been viewed'),
        ),
    ]