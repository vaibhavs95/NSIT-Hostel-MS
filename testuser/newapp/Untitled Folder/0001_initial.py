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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('userid', models.CharField(unique=True, verbose_name='user_id', max_length=255)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 2, 12, 18, 37, 4, 36978, tzinfo=utc))),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Caretaker',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name_of_caretaker', models.CharField(max_length=300)),
                ('caretaker_phone_num', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ChiefWarden',
            fields=[
                ('username', models.CharField(primary_key=True, serialize=False, default='', max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobno', models.CharField(max_length=15)),
                ('phoneno', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Closures',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('clo_or_ext', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('lodgers_roll_no', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('date_of_complaint', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.CharField(max_length=250)),
                ('fine_amount', models.IntegerField()),
                ('paid_or_not', models.BooleanField()),
                ('date_of_action', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hostels',
            fields=[
                ('username', models.CharField(primary_key=True, serialize=False, default='', max_length=20)),
                ('warden_name', models.CharField(default='', max_length=20)),
                ('hostel_name', models.CharField(default='', max_length=20)),
                ('room_capacity', models.IntegerField(null=True, blank=True)),
                ('room_available', models.IntegerField(null=True, blank=True)),
                ('warden_phone_num', models.CharField(max_length=20, null=True, blank=True)),
                ('warden_email', models.EmailField(max_length=254, null=True, blank=True)),
                ('warden_landLine', models.CharField(max_length=300, null=True, blank=True)),
                ('warden_portfolio', models.CharField(max_length=40, null=True, blank=True)),
                ('warden_department', models.CharField(max_length=20, null=True, blank=True)),
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
            name='PreviousHostelDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('room_no', models.CharField(max_length=10)),
                ('capacity_of_room', models.IntegerField()),
                ('student_no1', models.CharField(max_length=300, null=True)),
                ('student_no2', models.CharField(max_length=300, null=True)),
                ('student_no3', models.CharField(max_length=300, null=True)),
                ('filled_rooms', models.IntegerField(null=True)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('username', models.CharField(primary_key=True, serialize=False, default='', max_length=20)),
                ('name', models.CharField(default='', max_length=50)),
                ('date_of_birth', models.DateTimeField(default=datetime.datetime.now)),
                ('distance_from_nsit', models.IntegerField(default=0)),
                ('current_sem_join_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('current_hostel_join_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('college_category', models.CharField(choices=[('DGEN', 'Delhi General'), ('DOBC', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST')], default='DGEN', max_length=1)),
                ('blood_group', models.CharField(choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], default='B+', max_length=1)),
                ('fee_last_submitted', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('student_phone_num', models.CharField(max_length=20)),
                ('student_email', models.EmailField(unique=True, max_length=254)),
                ('student_optional_phone_num', models.CharField(max_length=20, null=True)),
                ('corpus_calculated_uptill', models.DateTimeField()),
                ('corpus', models.IntegerField(default=0)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('parent_email', models.EmailField(unique=True, max_length=254)),
                ('parent_phone_num', models.CharField(max_length=20)),
                ('parent_optional_phone_num', models.CharField(max_length=20, null=True)),
                ('permanent_address', models.CharField(max_length=200)),
                ('permanent_address_zipcode', models.IntegerField()),
                ('local_guardian_name', models.CharField(max_length=100, null=True)),
                ('local_guardian_address', models.CharField(max_length=200, null=True)),
                ('local_guardian_address_zipcode', models.IntegerField(null=True)),
                ('local_guardian_phone_num', models.CharField(max_length=20, null=True)),
                ('local_guardian_optional_phone_num', models.CharField(max_length=20, null=True)),
                ('local_guardian_email', models.EmailField(max_length=254, null=True)),
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
            field=models.ManyToManyField(to='newapp.Hostels'),
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
