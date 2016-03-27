# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_auto_20160327_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messdetail',
            name='hostel',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 26, 21, 30, 46, 716512, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='MessDetail',
        ),
    ]
