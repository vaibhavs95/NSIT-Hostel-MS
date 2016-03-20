# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0023_auto_20160316_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 16, 20, 7, 11, 441789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='permanent_address_zipcode',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
