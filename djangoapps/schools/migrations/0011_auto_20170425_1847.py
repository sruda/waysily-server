# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-25 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0010_school_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationoption',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, 'Homestay'), (2, 'Live with a local host'), (3, 'Hostel'), (4, 'Shared Apartment'), (5, 'Private Apartment'), (6, 'Room at the school')], default=1, verbose_name='Type of Accommodation'),
        ),
    ]
