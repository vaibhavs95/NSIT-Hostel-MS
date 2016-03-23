# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_auto_20160217_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostels',
            name='warden_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 2, 18, 6, 58, 37, 786149, tzinfo=utc)),
        ),
    ]
