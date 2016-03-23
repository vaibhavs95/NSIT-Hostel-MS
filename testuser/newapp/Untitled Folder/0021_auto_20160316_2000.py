# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0020_auto_20160316_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 16, 20, 0, 27, 574549, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='blood_group',
            field=models.CharField(default='B+', blank=True, max_length=1, choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')]),
        ),
        migrations.AlterField(
            model_name='students',
            name='college_category',
            field=models.CharField(default='DGEN', blank=True, max_length=1, choices=[('DGEN', 'Delhi General'), ('DOBC', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST')]),
        ),
        migrations.AlterField(
            model_name='students',
            name='corpus',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='corpus_calculated_uptill',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='current_hostel_join_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='current_sem_join_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='distance_from_nsit',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='father_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='fee_last_submitted',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(default='M', blank=True, max_length=1, choices=[('M', 'Male'), ('F', 'Female')]),
        ),
        migrations.AlterField(
            model_name='students',
            name='local_guardian_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='local_guardian_address_zipcode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='local_guardian_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='local_guardian_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='local_guardian_optional_phone_num',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='local_guardian_phone_num',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='mother_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(default='', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='students',
            name='parent_email',
            field=models.EmailField(unique=True, blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='students',
            name='parent_optional_phone_num',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='parent_phone_num',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='permanent_address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='permanent_address_zipcode',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_optional_phone_num',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_phone_num',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
