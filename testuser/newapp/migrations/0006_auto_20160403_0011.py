# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_auto_20160402_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 4, 2, 18, 41, 17, 51800, tzinfo=utc)),
        ),
    ]
