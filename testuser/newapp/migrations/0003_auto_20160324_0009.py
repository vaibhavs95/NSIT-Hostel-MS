# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20160323_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilities',
            name='title',
            field=models.CharField(unique=True, max_length=100, default='Facility Name'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 23, 18, 39, 41, 15711, tzinfo=utc)),
        ),
    ]
