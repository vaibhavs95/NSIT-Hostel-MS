# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.db.models.deletion
from django.utils.timezone import utc
import newapp.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('userid', models.CharField(unique=True, max_length=255, verbose_name='user_id')),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 17, 17, 13, 7, 751266, tzinfo=utc))),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=100, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('title', models.CharField(primary_key=True, max_length=20, default='', serialize=False)),
                ('name', models.CharField(max_length=100, default='COMPUTER SCIENCE AND ENGINEERING')),
                ('roll_code', models.CharField(max_length=5, default='')),
            ],
        ),
        migrations.CreateModel(
            name='ChiefWarden',
            fields=[
                ('username', models.CharField(primary_key=True, max_length=20, default='', serialize=False)),
                ('name', models.CharField(max_length=20, default='')),
                ('email', models.EmailField(max_length=254)),
                ('mobno', models.CharField(max_length=15)),
                ('phoneno', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Closures',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('clo_or_ext', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('lodgers_roll_no', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300, default='')),
                ('date_of_complaint', models.DateField(auto_now=True)),
                ('closed', models.BooleanField(default=False)),
                ('forwarded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.CharField(max_length=400)),
                ('fine_amount', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('date_of_action', models.DateField()),
                ('file', models.FileField(upload_to=newapp.models.CriminalRecordFile)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=100, default='')),
                ('description', models.TextField(max_length=1000, default='')),
                ('time', models.DateTimeField(default=datetime.datetime(2016, 4, 17, 17, 13, 7, 764275, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('facility_name', models.CharField(max_length=100, default='')),
                ('facility_description', models.TextField(default='')),
                ('photo', models.ImageField(null=True, blank=True, upload_to=newapp.models.facility_photo_name)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200, default='')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=newapp.models.form_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='HostelAttachDates',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('hostel_last_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='HostelCouncil',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, default='')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, default='')),
                ('position', models.CharField(max_length=100, default='')),
                ('committee', models.CharField(blank=True, max_length=100, default='', null=True)),
                ('photo', models.ImageField(null=True, blank=True, upload_to=newapp.models.council_photo_name)),
            ],
        ),
        migrations.CreateModel(
            name='Hostels',
            fields=[
                ('username', models.CharField(primary_key=True, max_length=20, default='', serialize=False)),
                ('name', models.CharField(max_length=50, default='', null=True)),
                ('hostel_name', models.CharField(max_length=20, default='')),
                ('semEndDate', models.DateField(default=datetime.datetime(2016, 4, 17, 17, 13, 7, 752452, tzinfo=utc))),
                ('room_capacity', models.IntegerField(null=True, blank=True)),
                ('room_available', models.IntegerField(null=True, blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('landline', models.CharField(max_length=300, null=True, blank=True)),
                ('portfolio', models.CharField(max_length=40, null=True, blank=True)),
                ('department', models.CharField(max_length=20, null=True, blank=True)),
                ('warden_photo', models.ImageField(null=True, blank=True, upload_to=newapp.models.warden_photo_name)),
                ('hostel_photo', models.ImageField(null=True, blank=True, upload_to=newapp.models.main_page_photo_name)),
                ('hostel_text', models.CharField(max_length=100, default='')),
                ('chief_warden', models.ForeignKey(to='newapp.ChiefWarden')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to=newapp.models.eventphotoname)),
                ('event', models.ForeignKey(to='newapp.Event', default=None)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MessDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=200, default=None)),
                ('file', models.FileField(null=True, upload_to=newapp.models.noticePhotoForm)),
                ('creator', models.CharField(max_length=30)),
                ('date', models.DateField(default=datetime.date(2016, 4, 17))),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('paymentDate', models.DateField()),
                ('receiptNumber', models.IntegerField()),
                ('paymentAmount', models.IntegerField()),
                ('bank', models.ForeignKey(to='newapp.Banks')),
            ],
        ),
        migrations.CreateModel(
            name='PreviousHostelDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('hostel_name', models.CharField(max_length=40)),
                ('room_no', models.CharField(max_length=10)),
                ('hostel_join_date', models.DateField()),
                ('hostel_leave_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('room_no', models.CharField(max_length=10)),
                ('capacity_of_room', models.IntegerField()),
                ('capacity_remaining', models.IntegerField(null=True, blank=True)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(unique=True, max_length=20, default='')),
                ('name', models.CharField(max_length=50, default='')),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 17, 17, 13, 7, 754514, tzinfo=utc))),
                ('distance_from_nsit', models.IntegerField(default=0)),
                ('current_hostel_join_date', models.DateField(default=datetime.datetime.now, blank=True)),
                ('gender', models.CharField(max_length=10, default='M', choices=[('M', 'Male'), ('F', 'Female')])),
                ('college_category', models.CharField(max_length=5, default='DGEN', choices=[('DGEN', 'Delhi General'), ('DOB', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST'), ('DKM', 'Delhi Kashmiri Migrant'), ('DDC', 'Delhi Defense Category'), ('DPH', 'Delhi Physically Handicapped'), ('DOP', 'Delhi OP'), ('OGEN', 'Outside Delhi General'), ('OOB', 'Outside Delhi OBC'), ('OSC', 'Outside Delhi SC'), ('OST', 'Outside Delhi ST'), ('OKM', 'Outside Delhi Kashmiri Migrant'), ('ODC', 'Outside Delhi Defense Category'), ('OPH', 'Outside Delhi Physically Handicapped'), ('OOP', 'Outside Delhi OP')])),
                ('blood_group', models.CharField(max_length=5, default='B+', choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')])),
                ('student_phone_num', models.CharField(max_length=20)),
                ('student_email', models.EmailField(unique=True, max_length=254)),
                ('student_optional_phone_num', models.CharField(max_length=20, null=True, blank=True)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('parent_email', models.EmailField(max_length=254)),
                ('parent_phone_num', models.CharField(max_length=20)),
                ('parent_optional_phone_num', models.CharField(max_length=20, null=True, blank=True)),
                ('permanent_address', models.CharField(max_length=200)),
                ('permanent_address_zipcode', models.IntegerField(default=0)),
                ('local_guardian_name', models.CharField(max_length=100, default='')),
                ('local_guardian_address', models.CharField(max_length=200, default='')),
                ('local_guardian_address_zipcode', models.IntegerField(default=0)),
                ('local_guardian_phone_num', models.CharField(max_length=20, default='')),
                ('local_guardian_optional_phone_num', models.CharField(max_length=20, default='', blank=True)),
                ('local_guardian_email', models.EmailField(max_length=254, default='')),
                ('student_photo', models.ImageField(upload_to=newapp.models.student_photo_name)),
                ('branch', models.ForeignKey(to='newapp.Branch')),
                ('room_number', models.ForeignKey(to='newapp.Rooms', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='previoushosteldetail',
            name='student',
            field=models.ForeignKey(to='newapp.Students', null=True, on_delete=django.db.models.deletion.SET_NULL),
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
            model_name='event',
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
