# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userid', models.CharField(unique=True, max_length=255, verbose_name='user_id')),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 3, 22, 22, 39, 51, 685064, tzinfo=utc))),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Caretaker',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name_of_caretaker', models.CharField(max_length=300)),
                ('caretaker_phone_num', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ChiefWarden',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=20, default='')),
                ('name', models.CharField(max_length=20, default='')),
                ('email', models.EmailField(max_length=254)),
                ('mobno', models.CharField(max_length=15)),
                ('phoneno', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Closures',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('clo_or_ext', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('lodgers_roll_no', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('date_of_complaint', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.CharField(max_length=250)),
                ('fine_amount', models.IntegerField()),
                ('paid_or_not', models.BooleanField()),
                ('date_of_action', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, default='Facility Name')),
                ('description', models.TextField(default='Facility Description')),
            ],
        ),
        migrations.CreateModel(
            name='Hostels',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=20, default='')),
                ('name', models.CharField(null=True, max_length=20, default='')),
                ('hostel_name', models.CharField(max_length=20, default='')),
                ('room_capacity', models.IntegerField(blank=True, null=True)),
                ('room_available', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, null=True, max_length=20)),
                ('email', models.EmailField(blank=True, null=True, max_length=254)),
                ('landline', models.CharField(blank=True, null=True, max_length=300)),
                ('portfolio', models.CharField(blank=True, null=True, max_length=40)),
                ('department', models.CharField(blank=True, null=True, max_length=20)),
                ('chief_warden', models.ForeignKey(to='newapp.ChiefWarden')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PreviousHostelDetail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('room_no', models.CharField(max_length=10)),
                ('hostel_join_date', models.DateTimeField()),
                ('hostel_leave_date', models.DateTimeField(default=datetime.datetime.now)),
                ('corpus_paid', models.IntegerField()),
                ('hostel_name', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('room_no', models.CharField(max_length=10)),
                ('capacity_of_room', models.IntegerField()),
                ('student_no1', models.CharField(blank=True, null=True, max_length=300)),
                ('student_no2', models.CharField(blank=True, null=True, max_length=300)),
                ('student_no3', models.CharField(blank=True, null=True, max_length=300)),
                ('capacity_remaining', models.IntegerField(blank=True, null=True)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=20, default='')),
                ('name', models.CharField(blank=True, max_length=50, default='')),
                ('date_of_birth', models.DateTimeField(default=datetime.datetime.now)),
                ('distance_from_nsit', models.IntegerField(blank=True, default=0)),
                ('current_sem_join_date', models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)),
                ('current_hostel_join_date', models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=10, default='M')),
                ('college_category', models.CharField(blank=True, choices=[('DGEN', 'Delhi General'), ('DOBC', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST')], max_length=5, default='DGEN')),
                ('blood_group', models.CharField(blank=True, choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], max_length=5, default='B+')),
                ('fee_last_submitted', models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)),
                ('student_phone_num', models.CharField(blank=True, max_length=20)),
                ('student_email', models.EmailField(unique=True, max_length=254)),
                ('student_optional_phone_num', models.CharField(blank=True, null=True, max_length=20)),
                ('corpus_calculated_uptill', models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)),
                ('corpus', models.IntegerField(blank=True, default=0)),
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
                ('branch', models.ForeignKey(to='newapp.Branch')),
                ('room_number', models.ForeignKey(to='newapp.Rooms')),
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
        migrations.AddField(
            model_name='caretaker',
            name='hostel',
            field=models.ForeignKey(to='newapp.Hostels'),
        ),
    ]
