# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_auto_20160327_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messdetail',
            name='weekday_lunch_charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 26, 21, 33, 26, 546031, tzinfo=utc)),
        ),
    ]
