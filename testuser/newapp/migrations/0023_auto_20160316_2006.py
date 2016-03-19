# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0022_auto_20160316_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 16, 20, 6, 30, 814067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='corpus_calculated_uptill',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, blank=True),
        ),
    ]
