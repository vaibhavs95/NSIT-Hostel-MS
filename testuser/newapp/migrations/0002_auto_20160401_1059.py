# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 4, 1, 5, 29, 33, 619263, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='room_number',
            field=models.ForeignKey(null=True, to='newapp.Rooms'),
        ),
    ]
