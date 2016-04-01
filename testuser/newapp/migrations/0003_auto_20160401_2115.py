# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20160401_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='previoushosteldetail',
            name='corpus_paid',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='student_no1',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='student_no2',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='student_no3',
        ),
        migrations.AlterField(
            model_name='closures',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='closures',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='date_of_complaint',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='criminalrecord',
            name='date_of_action',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 4, 1, 15, 45, 38, 274385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='previoushosteldetail',
            name='hostel_join_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='previoushosteldetail',
            name='hostel_leave_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='students',
            name='current_hostel_join_date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
