# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_auto_20160403_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 4, 3, 15, 9, 55, 271148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
