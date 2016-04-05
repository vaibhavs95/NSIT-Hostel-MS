# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import newapp.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('userid', models.CharField(verbose_name='user_id', unique=True, max_length=255)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 4, 20, 34, 31, 78130, tzinfo=utc))),
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
                ('title', models.CharField(serialize=False, primary_key=True, default='', max_length=20)),
                ('name', models.CharField(default='COMPUTER SCIENCE AND ENGINEERING', max_length=100)),
                ('roll_code', models.CharField(default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ChiefWarden',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, default='', max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobno', models.CharField(max_length=15)),
                ('phoneno', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Closures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('clo_or_ext', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('lodgers_roll_no', models.CharField(max_length=300)),
                ('description', models.CharField(default='', max_length=300)),
                ('date_of_complaint', models.DateField(auto_now=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('description', models.CharField(max_length=400)),
                ('fine_amount', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('date_of_action', models.DateField()),
                ('file', models.FileField(upload_to=newapp.models.CriminalRecordFile)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('facility_name', models.CharField(unique=True, default='', max_length=100)),
                ('facility_description', models.TextField(default='')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=newapp.models.facility_photo_name)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(default='', max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=newapp.models.form_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='HostelCouncil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(blank=True, default='', null=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=15)),
                ('position', models.CharField(default='', max_length=100)),
                ('committee', models.CharField(blank=True, default='', null=True, max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=newapp.models.council_photo_name)),
            ],
        ),
        migrations.CreateModel(
            name='Hostels',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, default='', max_length=20)),
                ('name', models.CharField(default='', null=True, max_length=50)),
                ('hostel_name', models.CharField(default='', max_length=20)),
                ('room_capacity', models.IntegerField(blank=True, null=True)),
                ('room_available', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, null=True, max_length=20)),
                ('email', models.EmailField(blank=True, null=True, max_length=254)),
                ('landline', models.CharField(blank=True, null=True, max_length=300)),
                ('portfolio', models.CharField(blank=True, null=True, max_length=40)),
                ('department', models.CharField(blank=True, null=True, max_length=20)),
                ('warden_photo', models.ImageField(blank=True, null=True, upload_to=newapp.models.warden_photo_name)),
                ('chief_warden', models.ForeignKey(to='newapp.ChiefWarden')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MessDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(unique=True, default=None, max_length=200)),
                ('file', models.FileField(null=True, upload_to=newapp.models.noticePhotoForm)),
                ('creator', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PreviousHostelDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('hostel_name', models.CharField(max_length=40)),
                ('room_no', models.CharField(max_length=10)),
                ('hostel_join_date', models.DateField()),
                ('hostel_leave_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('room_no', models.CharField(max_length=10)),
                ('capacity_of_room', models.IntegerField()),
                ('capacity_remaining', models.IntegerField(blank=True, null=True)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, default='', max_length=20)),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 4, 20, 34, 31, 81668, tzinfo=utc))),
                ('distance_from_nsit', models.IntegerField(blank=True, default=0)),
                ('current_hostel_join_date', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], blank=True, default='M', max_length=10)),
                ('college_category', models.CharField(choices=[('DGEN', 'Delhi General'), ('DOBC', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST')], blank=True, default='DGEN', max_length=5)),
                ('blood_group', models.CharField(choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], blank=True, default='B+', max_length=5)),
                ('student_phone_num', models.CharField(blank=True, max_length=20)),
                ('student_email', models.EmailField(unique=True, max_length=254)),
                ('student_optional_phone_num', models.CharField(blank=True, null=True, max_length=20)),
                ('father_name', models.CharField(blank=True, max_length=100)),
                ('mother_name', models.CharField(blank=True, max_length=100)),
                ('parent_email', models.EmailField(blank=True, max_length=254)),
                ('parent_phone_num', models.CharField(blank=True, max_length=20)),
                ('parent_optional_phone_num', models.CharField(blank=True, null=True, max_length=20)),
                ('permanent_address', models.CharField(blank=True, max_length=200)),
                ('permanent_address_zipcode', models.IntegerField(blank=True, null=True)),
                ('local_guardian_name', models.CharField(blank=True, null=True, max_length=100)),
                ('local_guardian_address', models.CharField(blank=True, null=True, max_length=200)),
                ('local_guardian_address_zipcode', models.IntegerField(blank=True, null=True)),
                ('local_guardian_phone_num', models.CharField(blank=True, null=True, max_length=20)),
                ('local_guardian_optional_phone_num', models.CharField(blank=True, null=True, max_length=20)),
                ('local_guardian_email', models.EmailField(blank=True, null=True, max_length=254)),
                ('student_photo', models.ImageField(blank=True, null=True, upload_to=newapp.models.student_photo_name)),
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