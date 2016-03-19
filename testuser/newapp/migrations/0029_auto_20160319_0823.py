# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0028_auto_20160319_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostels',
            name='landline',
            field=models.CharField(null=True, blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='hostels',
            name='phone',
            field=models.CharField(null=True, blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 19, 8, 23, 9, 969352, tzinfo=utc)),
        ),
    ]
