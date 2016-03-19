# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0019_auto_20160316_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='filled_rooms',
            new_name='capacity_remaining',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 16, 18, 40, 41, 337817, tzinfo=utc)),
        ),
    ]
