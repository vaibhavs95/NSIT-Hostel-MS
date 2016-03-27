# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_auto_20160327_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messdetail',
            name='wd_bf',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='messdetail',
            name='wd_l',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='messdetail',
            name='wd_s',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 26, 20, 56, 18, 878156, tzinfo=utc)),
        ),
    ]
