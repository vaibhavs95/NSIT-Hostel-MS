# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0010_auto_20160327_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facilities',
            name='description',
        ),
        migrations.RemoveField(
            model_name='facilities',
            name='title',
        ),
        migrations.AddField(
            model_name='facilities',
            name='facility_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='facilities',
            name='facility_name',
            field=models.CharField(unique=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 28, 19, 51, 57, 498331, tzinfo=utc)),
        ),
    ]
