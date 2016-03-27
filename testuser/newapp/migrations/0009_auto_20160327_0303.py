# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0008_auto_20160327_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messdetail',
            name='weekday_breakfast_charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='messdetail',
            name='weekday_dinner_charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='messdetail',
            name='weekday_snack_charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='messdetail',
            name='weekend_breakfast_charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='messdetail',
            name='weekend_dinner_charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='messdetail',
            name='weekend_lunch_charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='messdetail',
            name='weekend_snack_charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 26, 21, 33, 2, 537986, tzinfo=utc)),
        ),
    ]
