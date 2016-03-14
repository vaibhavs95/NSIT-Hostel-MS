# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_auto_20160212_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefwarden',
            name='name',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 2, 12, 18, 58, 19, 789962, tzinfo=utc)),
        ),
    ]
