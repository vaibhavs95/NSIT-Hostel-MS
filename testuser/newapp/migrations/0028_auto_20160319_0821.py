# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0027_auto_20160319_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostels',
            name='landline',
            field=models.IntegerField(max_length=300, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hostels',
            name='phone',
            field=models.IntegerField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 19, 8, 21, 26, 675602, tzinfo=utc)),
        ),
    ]
