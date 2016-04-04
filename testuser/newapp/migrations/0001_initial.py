# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import newapp.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('userid', models.CharField(verbose_name='user_id', max_length=255, unique=True)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 4, 11, 40, 7, 418661, tzinfo=utc))),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('title', models.CharField(default='', serialize=False, primary_key=True, max_length=20)),
                ('name', models.CharField(default='COMPUTER SCIENCE AND ENGINEERING', max_length=100)),
                ('roll_code', models.CharField(default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ChiefWarden',
            fields=[
                ('username', models.CharField(default='', serialize=False, primary_key=True, max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobno', models.CharField(max_length=15)),
                ('phoneno', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Closures',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('clo_or_ext', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('lodgers_roll_no', models.CharField(max_length=300)),
                ('description', models.CharField(default='', max_length=300)),
                ('date_of_complaint', models.DateField(auto_now=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.CharField(max_length=250)),
                ('fine_amount', models.IntegerField()),
                ('paid_or_not', models.BooleanField()),
                ('date_of_action', models.DateField(default=datetime.datetime.now)),
                ('file', models.FileField(upload_to=newapp.models.CriminalRecordFile, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('facility_name', models.CharField(default='', unique=True, max_length=100)),
                ('facility_description', models.TextField(default='')),
                ('photo', models.ImageField(blank=True, upload_to=newapp.models.facility_photo_name, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(default='', max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=newapp.models.form_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='HostelCouncil',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100, blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=15)),
                ('position', models.CharField(default='', max_length=100)),
                ('committee', models.CharField(default='', max_length=100, blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to=newapp.models.council_photo_name, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hostels',
            fields=[
                ('username', models.CharField(default='', serialize=False, primary_key=True, max_length=20)),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('hostel_name', models.CharField(default='', max_length=20)),
                ('room_capacity', models.IntegerField(blank=True, null=True)),
                ('room_available', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20, blank=True, null=True)),
                ('email', models.EmailField(max_length=254, blank=True, null=True)),
                ('landline', models.CharField(max_length=300, blank=True, null=True)),
                ('portfolio', models.CharField(max_length=40, blank=True, null=True)),
                ('department', models.CharField(max_length=20, blank=True, null=True)),
                ('warden_photo', models.ImageField(blank=True, upload_to=newapp.models.warden_photo_name, null=True)),
                ('chief_warden', models.ForeignKey(to='newapp.ChiefWarden')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MessDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('weekday_breakfast_charge', models.IntegerField()),
                ('weekday_lunch_charge', models.IntegerField()),
                ('weekday_snack_charge', models.IntegerField()),
                ('weekday_dinner_charge', models.IntegerField()),
                ('weekend_breakfast_charge', models.IntegerField()),
                ('weekend_lunch_charge', models.IntegerField()),
                ('weekend_snack_charge', models.IntegerField()),
                ('weekend_dinner_charge', models.IntegerField()),
                ('menu', models.FileField(upload_to=newapp.models.messmenu_file_name)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(default=None, unique=True, max_length=200)),
                ('file', models.FileField(upload_to=newapp.models.noticePhotoForm, null=True)),
                ('creator', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PreviousHostelDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('hostel_name', models.CharField(max_length=40)),
                ('room_no', models.CharField(max_length=10)),
                ('hostel_join_date', models.DateField()),
                ('hostel_leave_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('room_no', models.CharField(max_length=10)),
                ('capacity_of_room', models.IntegerField()),
                ('capacity_remaining', models.IntegerField(blank=True, null=True)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('username', models.CharField(default='', serialize=False, primary_key=True, max_length=20)),
                ('name', models.CharField(default='', max_length=50, blank=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('distance_from_nsit', models.IntegerField(default=0, blank=True)),
                ('current_hostel_join_date', models.DateField(default=datetime.datetime.now, blank=True, null=True)),
                ('gender', models.CharField(default='M', max_length=10, blank=True, choices=[('M', 'Male'), ('F', 'Female')])),
                ('college_category', models.CharField(default='DGEN', max_length=5, blank=True, choices=[('DGEN', 'Delhi General'), ('DOBC', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST')])),
                ('blood_group', models.CharField(default='B+', max_length=5, blank=True, choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')])),
                ('student_phone_num', models.CharField(max_length=20, blank=True)),
                ('student_email', models.EmailField(unique=True, max_length=254)),
                ('student_optional_phone_num', models.CharField(max_length=20, blank=True, null=True)),
                ('father_name', models.CharField(max_length=100, blank=True)),
                ('mother_name', models.CharField(max_length=100, blank=True)),
                ('parent_email', models.EmailField(max_length=254, blank=True)),
                ('parent_phone_num', models.CharField(max_length=20, blank=True)),
                ('parent_optional_phone_num', models.CharField(max_length=20, blank=True, null=True)),
                ('permanent_address', models.CharField(max_length=200, blank=True)),
                ('permanent_address_zipcode', models.IntegerField(blank=True, null=True)),
                ('local_guardian_name', models.CharField(max_length=100, blank=True, null=True)),
                ('local_guardian_address', models.CharField(max_length=200, blank=True, null=True)),
                ('local_guardian_address_zipcode', models.IntegerField(blank=True, null=True)),
                ('local_guardian_phone_num', models.CharField(max_length=20, blank=True, null=True)),
                ('local_guardian_optional_phone_num', models.CharField(max_length=20, blank=True, null=True)),
                ('local_guardian_email', models.EmailField(max_length=254, blank=True, null=True)),
                ('student_photo', models.ImageField(blank=True, upload_to=newapp.models.student_photo_name, null=True)),
                ('branch', models.ForeignKey(to='newapp.Branch')),
                ('room_number', models.ForeignKey(to='newapp.Rooms', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='previoushosteldetail',
            name='student',
            field=models.ForeignKey(to='newapp.Students'),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='student',
            field=models.ForeignKey(to='newapp.Students'),
        ),
        migrations.AddField(
            model_name='hostelcouncil',
            name='hostel',
            field=models.ForeignKey(to='newapp.Hostels'),
        ),
        migrations.AddField(
            model_name='form',
            name='hostel',
            field=models.ForeignKey(to='newapp.Hostels'),
        ),
        migrations.AddField(
            model_name='facilities',
            name='hostel',
            field=models.ForeignKey(to='newapp.Hostels'),
        ),
        migrations.AddField(
            model_name='criminalrecord',
            name='student',
            field=models.ForeignKey(to='newapp.Students'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='hostel',
            field=models.ForeignKey(to='newapp.Hostels'),
        ),
        migrations.AddField(
            model_name='closures',
            name='hostel',
            field=models.ManyToManyField(to='newapp.Hostels'),
        ),
    ]
