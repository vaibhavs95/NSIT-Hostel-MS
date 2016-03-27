# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import newapp.models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_auto_20160327_0300'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessDetail',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('weekday_breakfast_from', models.TimeField()),
                ('weekday_breakfast_to', models.TimeField()),
                ('weekday_lunch_from', models.TimeField()),
                ('weekday_lunch_to', models.TimeField()),
                ('weekday_snack_from', models.TimeField()),
                ('weekday_snack_to', models.TimeField()),
                ('weekday_dinner_from', models.TimeField()),
                ('weekday_dinner_to', models.TimeField()),
                ('weekend_breakfast_from', models.TimeField()),
                ('weekend_breakfast_to', models.TimeField()),
                ('weekend_lunch_from', models.TimeField()),
                ('weekend_lunch_to', models.TimeField()),
                ('weekend_snack_from', models.TimeField()),
                ('weekend_snack_to', models.TimeField()),
                ('weekend_dinner_from', models.TimeField()),
                ('weekend_dinner_to', models.TimeField()),
                ('weekday_breakfast_charge', models.TimeField()),
                ('weekday_lunch_charge', models.TimeField()),
                ('weekday_snack_charge', models.TimeField()),
                ('weekday_dinner_charge', models.TimeField()),
                ('weekend_breakfast_charge', models.TimeField()),
                ('weekend_lunch_charge', models.TimeField()),
                ('weekend_snack_charge', models.TimeField()),
                ('weekend_dinner_charge', models.TimeField()),
                ('menu', models.FileField(upload_to=newapp.models.messmenu_file_name)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 26, 21, 31, 38, 331175, tzinfo=utc)),
        ),
    ]
