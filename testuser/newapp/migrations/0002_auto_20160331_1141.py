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
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 31, 6, 11, 45, 869550, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(unique=True, default=None, max_length=200),
        ),
    ]
