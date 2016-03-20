# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0015_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 15, 15, 30, 56, 395492, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='filled_rooms',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='student_no1',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='student_no2',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='student_no3',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
