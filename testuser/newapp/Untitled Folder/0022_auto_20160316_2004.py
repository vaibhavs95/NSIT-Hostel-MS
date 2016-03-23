# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0021_auto_20160316_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 16, 20, 4, 30, 908799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='blood_group',
            field=models.CharField(choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], blank=True, default='B+', max_length=5),
        ),
        migrations.AlterField(
            model_name='students',
            name='college_category',
            field=models.CharField(choices=[('DGEN', 'Delhi General'), ('DOBC', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST')], blank=True, default='DGEN', max_length=5),
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], blank=True, default='M', max_length=10),
        ),
    ]
