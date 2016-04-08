# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
<<<<<<< HEAD
import datetime
=======
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
import newapp.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('userid', models.CharField(verbose_name='user_id', max_length=255, unique=True)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 6, 20, 27, 55, 933255, tzinfo=utc))),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userid', models.CharField(max_length=255, verbose_name='user_id', unique=True)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 7, 19, 5, 33, 331435, tzinfo=utc))),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, default='', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
<<<<<<< HEAD
                ('title', models.CharField(max_length=20, default='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, default='COMPUTER SCIENCE AND ENGINEERING')),
                ('roll_code', models.CharField(max_length=5, default='')),
=======
                ('title', models.CharField(primary_key=True, serialize=False, default='', max_length=20)),
                ('name', models.CharField(default='COMPUTER SCIENCE AND ENGINEERING', max_length=100)),
                ('roll_code', models.CharField(default='', max_length=5)),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
            ],
        ),
        migrations.CreateModel(
            name='ChiefWarden',
            fields=[
<<<<<<< HEAD
                ('username', models.CharField(max_length=20, default='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, default='')),
=======
                ('username', models.CharField(primary_key=True, serialize=False, default='', max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('email', models.EmailField(max_length=254)),
                ('mobno', models.CharField(max_length=15)),
                ('phoneno', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Closures',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('clo_or_ext', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('lodgers_roll_no', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300, default='')),
                ('date_of_complaint', models.DateField(auto_now=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
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
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('facility_name', models.CharField(max_length=100, default='')),
                ('facility_description', models.TextField(default='')),
                ('photo', models.ImageField(blank=True, upload_to=newapp.models.facility_photo_name, null=True)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=100, default='', unique=True)),
                ('facility_description', models.TextField(default='')),
                ('photo', models.ImageField(upload_to=newapp.models.facility_photo_name, blank=True, null=True)),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, default='')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=newapp.models.form_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='HostelAttachDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_last_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='HostelCouncil',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, default='')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, default='')),
                ('position', models.CharField(max_length=100, default='')),
                ('committee', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, upload_to=newapp.models.council_photo_name, null=True)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True, default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=15)),
                ('position', models.CharField(default='', max_length=100)),
                ('committee', models.CharField(blank=True, null=True, default='', max_length=100)),
                ('photo', models.ImageField(upload_to=newapp.models.council_photo_name, blank=True, null=True)),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
            ],
        ),
        migrations.CreateModel(
            name='Hostels',
            fields=[
<<<<<<< HEAD
                ('username', models.CharField(max_length=20, default='', primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('hostel_name', models.CharField(max_length=20, default='')),
                ('room_capacity', models.IntegerField(blank=True, null=True)),
                ('room_available', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('landline', models.CharField(blank=True, max_length=300, null=True)),
                ('portfolio', models.CharField(blank=True, max_length=40, null=True)),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('warden_photo', models.ImageField(blank=True, upload_to=newapp.models.warden_photo_name, null=True)),
=======
                ('username', models.CharField(primary_key=True, serialize=False, default='', max_length=20)),
                ('name', models.CharField(null=True, default='', max_length=50)),
                ('hostel_name', models.CharField(default='', max_length=20)),
                ('semEndDate', models.DateField(default=datetime.datetime(2016, 4, 7, 19, 5, 33, 333023, tzinfo=utc))),
                ('room_capacity', models.IntegerField(blank=True, null=True)),
                ('room_available', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, null=True, max_length=20)),
                ('email', models.EmailField(blank=True, null=True, max_length=254)),
                ('landline', models.CharField(blank=True, null=True, max_length=300)),
                ('portfolio', models.CharField(blank=True, null=True, max_length=40)),
                ('department', models.CharField(blank=True, null=True, max_length=20)),
                ('warden_photo', models.ImageField(upload_to=newapp.models.warden_photo_name, blank=True, null=True)),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('chief_warden', models.ForeignKey(to='newapp.ChiefWarden')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MessDetail',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
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
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True, default=None)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, default=None, unique=True)),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('file', models.FileField(upload_to=newapp.models.noticePhotoForm, null=True)),
                ('creator', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentDate', models.DateField()),
                ('receiptNumber', models.IntegerField()),
                ('bank', models.ForeignKey(to='newapp.Banks')),
            ],
        ),
        migrations.CreateModel(
            name='PreviousHostelDetail',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('hostel_name', models.CharField(max_length=40)),
                ('room_no', models.CharField(max_length=10)),
                ('hostel_join_date', models.DateField()),
                ('hostel_leave_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('room_no', models.CharField(max_length=10)),
                ('capacity_of_room', models.IntegerField()),
                ('capacity_remaining', models.IntegerField(blank=True, null=True)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, default='')),
                ('name', models.CharField(blank=True, max_length=50, default='')),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 6, 20, 27, 55, 936054, tzinfo=utc))),
                ('distance_from_nsit', models.IntegerField(blank=True, default=0)),
                ('current_hostel_join_date', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default='M')),
                ('college_category', models.CharField(blank=True, max_length=5, choices=[('DGEN', 'Delhi General'), ('DOBC', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST')], default='DGEN')),
                ('blood_group', models.CharField(blank=True, max_length=5, choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], default='B+')),
                ('student_phone_num', models.CharField(blank=True, max_length=20)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_optional_phone_num', models.CharField(blank=True, max_length=20, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100)),
                ('mother_name', models.CharField(blank=True, max_length=100)),
                ('parent_email', models.EmailField(blank=True, max_length=254)),
                ('parent_phone_num', models.CharField(blank=True, max_length=20)),
                ('parent_optional_phone_num', models.CharField(blank=True, max_length=20, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=200)),
                ('permanent_address_zipcode', models.IntegerField(blank=True, null=True)),
                ('local_guardian_name', models.CharField(blank=True, max_length=100, null=True)),
                ('local_guardian_address', models.CharField(blank=True, max_length=200, null=True)),
                ('local_guardian_address_zipcode', models.IntegerField(blank=True, null=True)),
                ('local_guardian_phone_num', models.CharField(blank=True, max_length=20, null=True)),
                ('local_guardian_optional_phone_num', models.CharField(blank=True, max_length=20, null=True)),
                ('local_guardian_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('student_photo', models.ImageField(blank=True, upload_to=newapp.models.student_photo_name, null=True)),
=======
                ('username', models.CharField(primary_key=True, serialize=False, default='', max_length=20)),
                ('name', models.CharField(default='', max_length=50)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 7, 19, 5, 33, 335167, tzinfo=utc))),
                ('distance_from_nsit', models.IntegerField(default=0)),
                ('current_hostel_join_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10)),
                ('college_category', models.CharField(choices=[('DGEN', 'Delhi General'), ('DOB', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST'), ('DKM', 'Delhi Kashmiri Migrant'), ('DDC', 'Delhi Defense Category'), ('DPH', 'Delhi Physically Handicapped'), ('DOP', 'Delhi OP'), ('OGEN', 'Outside Delhi General'), ('OOB', 'Outside Delhi OBC'), ('OSC', 'Outside Delhi SC'), ('OST', 'Outside Delhi ST'), ('OKM', 'Outside Delhi Kashmiri Migrant'), ('ODC', 'Outside Delhi Defense Category'), ('OPH', 'Outside Delhi Physically Handicapped'), ('OOP', 'Outside Delhi OP')], default='DGEN', max_length=5)),
                ('blood_group', models.CharField(choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], default='B+', max_length=5)),
                ('student_phone_num', models.CharField(max_length=20)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_optional_phone_num', models.CharField(blank=True, null=True, max_length=20)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('parent_email', models.EmailField(max_length=254)),
                ('parent_phone_num', models.CharField(max_length=20)),
                ('parent_optional_phone_num', models.CharField(blank=True, null=True, max_length=20)),
                ('permanent_address', models.CharField(max_length=200)),
                ('permanent_address_zipcode', models.IntegerField(blank=True, null=True)),
                ('local_guardian_name', models.CharField(default='', max_length=100)),
                ('local_guardian_address', models.CharField(default='', max_length=200)),
                ('local_guardian_address_zipcode', models.IntegerField(default=0)),
                ('local_guardian_phone_num', models.CharField(default='', max_length=20)),
                ('local_guardian_optional_phone_num', models.CharField(blank=True, default='', max_length=20)),
                ('local_guardian_email', models.EmailField(default='', max_length=254)),
                ('student_photo', models.ImageField(upload_to=newapp.models.student_photo_name, blank=True, null=True)),
>>>>>>> 608a2bb0b8ceeac023d91daaaf39bfc47abe378b
                ('branch', models.ForeignKey(to='newapp.Branch')),
                ('room_number', models.ForeignKey(null=True, to='newapp.Rooms')),
            ],
        ),
        migrations.AddField(
            model_name='previoushosteldetail',
            name='student',
            field=models.ForeignKey(to='newapp.Students'),
        ),
        migrations.AddField(
            model_name='paymentdetails',
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
            model_name='hostelattachdates',
            name='student',
            field=models.ForeignKey(to='newapp.Students'),
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
