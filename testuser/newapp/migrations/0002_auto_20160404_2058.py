# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminalrecord',
            name='paid_or_not',
        ),
        migrations.AddField(
            model_name='criminalrecord',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='criminalrecord',
            name='date_of_action',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='criminalrecord',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 4, 4, 15, 28, 37, 922957, tzinfo=utc)),
        ),
    ]
