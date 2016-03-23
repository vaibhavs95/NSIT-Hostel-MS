# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0025_auto_20160316_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 16, 20, 10, 11, 379741, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='parent_email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
