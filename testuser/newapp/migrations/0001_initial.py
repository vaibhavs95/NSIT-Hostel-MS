# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.db.models.deletion
<<<<<<< HEAD
import newapp.models
from django.utils.timezone import utc
=======
from django.utils.timezone import utc
import newapp.models
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('userid', models.CharField(unique=True, verbose_name='user_id', max_length=255)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 11, 18, 20, 47, 238829, tzinfo=utc))),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('userid', models.CharField(verbose_name='user_id', unique=True, max_length=255)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 16, 7, 33, 54, 63390, tzinfo=utc))),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
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
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(default='', unique=True, max_length=100)),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True, default='')),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
<<<<<<< HEAD
                ('title', models.CharField(default='', serialize=False, primary_key=True, max_length=20)),
                ('name', models.CharField(default='COMPUTER SCIENCE AND ENGINEERING', max_length=100)),
                ('roll_code', models.CharField(default='', max_length=5)),
=======
                ('title', models.CharField(serialize=False, max_length=20, default='', primary_key=True)),
                ('name', models.CharField(max_length=100, default='COMPUTER SCIENCE AND ENGINEERING')),
                ('roll_code', models.CharField(max_length=5, default='')),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
            ],
        ),
        migrations.CreateModel(
            name='ChiefWarden',
            fields=[
<<<<<<< HEAD
                ('username', models.CharField(default='', serialize=False, primary_key=True, max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
=======
                ('username', models.CharField(serialize=False, max_length=20, default='', primary_key=True)),
                ('name', models.CharField(max_length=20, default='')),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('email', models.EmailField(max_length=254)),
                ('mobno', models.CharField(max_length=15)),
                ('phoneno', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Closures',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('clo_or_ext', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('lodgers_roll_no', models.CharField(max_length=300)),
                ('description', models.CharField(default='', max_length=300)),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('lodgers_roll_no', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300, default='')),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('date_of_complaint', models.DateField(auto_now=True)),
                ('closed', models.BooleanField(default=False)),
                ('forwarded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
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
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(default='', unique=True, max_length=100)),
                ('description', models.TextField(default='', max_length=1000)),
                ('time', models.DateTimeField(default=datetime.datetime(2016, 4, 11, 18, 20, 47, 254330, tzinfo=utc))),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, unique=True, default='')),
                ('description', models.TextField(max_length=1000, default='')),
                ('time', models.DateTimeField(default=datetime.datetime(2016, 4, 16, 7, 33, 54, 75992, tzinfo=utc))),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('facility_name', models.CharField(default='', max_length=100)),
                ('facility_description', models.TextField(default='')),
                ('photo', models.ImageField(upload_to=newapp.models.facility_photo_name, blank=True, null=True)),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('facility_name', models.CharField(max_length=100, default='')),
                ('facility_description', models.TextField(default='')),
                ('photo', models.ImageField(upload_to=newapp.models.facility_photo_name, null=True, blank=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, default='')),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=newapp.models.form_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='HostelAttachDates',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('hostel_last_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='HostelCouncil',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=15)),
                ('position', models.CharField(default='', max_length=100)),
                ('committee', models.CharField(default='', blank=True, null=True, max_length=100)),
                ('photo', models.ImageField(upload_to=newapp.models.council_photo_name, blank=True, null=True)),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, default='')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, default='')),
                ('position', models.CharField(max_length=100, default='')),
                ('committee', models.CharField(max_length=100, null=True, default='', blank=True)),
                ('photo', models.ImageField(upload_to=newapp.models.council_photo_name, null=True, blank=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
            ],
        ),
        migrations.CreateModel(
            name='Hostels',
            fields=[
<<<<<<< HEAD
                ('username', models.CharField(default='', serialize=False, primary_key=True, max_length=20)),
                ('name', models.CharField(default='', null=True, max_length=50)),
                ('hostel_name', models.CharField(default='', max_length=20)),
                ('semEndDate', models.DateField(default=datetime.datetime(2016, 4, 11, 18, 20, 47, 240263, tzinfo=utc))),
                ('room_capacity', models.IntegerField(blank=True, null=True)),
                ('room_available', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, null=True, max_length=20)),
                ('email', models.EmailField(blank=True, null=True, max_length=254)),
                ('landline', models.CharField(blank=True, null=True, max_length=300)),
                ('portfolio', models.CharField(blank=True, null=True, max_length=40)),
                ('department', models.CharField(blank=True, null=True, max_length=20)),
                ('warden_photo', models.ImageField(upload_to=newapp.models.warden_photo_name, blank=True, null=True)),
=======
                ('username', models.CharField(serialize=False, max_length=20, default='', primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, default='')),
                ('hostel_name', models.CharField(max_length=20, default='')),
                ('semEndDate', models.DateField(default=datetime.datetime(2016, 4, 16, 7, 33, 54, 64507, tzinfo=utc))),
                ('room_capacity', models.IntegerField(null=True, blank=True)),
                ('room_available', models.IntegerField(null=True, blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('landline', models.CharField(max_length=300, null=True, blank=True)),
                ('portfolio', models.CharField(max_length=40, null=True, blank=True)),
                ('department', models.CharField(max_length=20, null=True, blank=True)),
                ('warden_photo', models.ImageField(upload_to=newapp.models.warden_photo_name, null=True, blank=True)),
                ('hostel_photo', models.ImageField(upload_to=newapp.models.main_page_photo_name, null=True, blank=True)),
                ('hostel_text', models.CharField(max_length=100, default='')),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('chief_warden', models.ForeignKey(to='newapp.ChiefWarden')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to=newapp.models.eventphotoname)),
                ('event', models.ForeignKey(default=None, to='newapp.Event')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=newapp.models.eventphotoname)),
                ('event', models.ForeignKey(to='newapp.Event', default=None)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MessDetail',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(default=None, unique=True, max_length=200)),
                ('file', models.FileField(upload_to=newapp.models.noticePhotoForm, null=True)),
                ('creator', models.CharField(max_length=30)),
                ('date', models.DateField(default=datetime.date(2016, 4, 11))),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, unique=True, default=None)),
                ('file', models.FileField(upload_to=newapp.models.noticePhotoForm, null=True)),
                ('creator', models.CharField(max_length=30)),
                ('date', models.DateField(default=datetime.date(2016, 4, 16))),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('paymentDate', models.DateField()),
                ('receiptNumber', models.IntegerField()),
                ('bank', models.ForeignKey(to='newapp.Banks')),
            ],
        ),
        migrations.CreateModel(
            name='PreviousHostelDetail',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('room_no', models.CharField(max_length=10)),
                ('capacity_of_room', models.IntegerField()),
                ('capacity_remaining', models.IntegerField(blank=True, null=True)),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('room_no', models.CharField(max_length=10)),
                ('capacity_of_room', models.IntegerField()),
                ('capacity_remaining', models.IntegerField(null=True, blank=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('username', models.CharField(default='', unique=True, max_length=20)),
                ('name', models.CharField(default='', max_length=50)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 11, 18, 20, 47, 242590, tzinfo=utc))),
                ('distance_from_nsit', models.IntegerField(default=0)),
                ('current_hostel_join_date', models.DateField(default=datetime.datetime.now, blank=True)),
                ('gender', models.CharField(default='M', choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('college_category', models.CharField(default='DGEN', choices=[('DGEN', 'Delhi General'), ('DOB', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST'), ('DKM', 'Delhi Kashmiri Migrant'), ('DDC', 'Delhi Defense Category'), ('DPH', 'Delhi Physically Handicapped'), ('DOP', 'Delhi OP'), ('OGEN', 'Outside Delhi General'), ('OOB', 'Outside Delhi OBC'), ('OSC', 'Outside Delhi SC'), ('OST', 'Outside Delhi ST'), ('OKM', 'Outside Delhi Kashmiri Migrant'), ('ODC', 'Outside Delhi Defense Category'), ('OPH', 'Outside Delhi Physically Handicapped'), ('OOP', 'Outside Delhi OP')], max_length=5)),
                ('blood_group', models.CharField(default='B+', choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], max_length=5)),
                ('student_phone_num', models.CharField(max_length=20)),
                ('student_email', models.EmailField(unique=True, max_length=254)),
                ('student_optional_phone_num', models.CharField(blank=True, null=True, max_length=20)),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, unique=True, default='')),
                ('name', models.CharField(max_length=50, default='')),
                ('date_of_birth', models.DateField(default=datetime.datetime(2016, 4, 16, 7, 33, 54, 66600, tzinfo=utc))),
                ('distance_from_nsit', models.IntegerField(default=0)),
                ('current_hostel_join_date', models.DateField(default=datetime.datetime.now, blank=True)),
                ('gender', models.CharField(max_length=10, default='M', choices=[('M', 'Male'), ('F', 'Female')])),
                ('college_category', models.CharField(max_length=5, default='DGEN', choices=[('DGEN', 'Delhi General'), ('DOB', 'Delhi OBC'), ('DSC', 'Delhi SC'), ('DST', 'Delhi ST'), ('DKM', 'Delhi Kashmiri Migrant'), ('DDC', 'Delhi Defense Category'), ('DPH', 'Delhi Physically Handicapped'), ('DOP', 'Delhi OP'), ('OGEN', 'Outside Delhi General'), ('OOB', 'Outside Delhi OBC'), ('OSC', 'Outside Delhi SC'), ('OST', 'Outside Delhi ST'), ('OKM', 'Outside Delhi Kashmiri Migrant'), ('ODC', 'Outside Delhi Defense Category'), ('OPH', 'Outside Delhi Physically Handicapped'), ('OOP', 'Outside Delhi OP')])),
                ('blood_group', models.CharField(max_length=5, default='B+', choices=[('B+', 'B Positive'), ('A+', 'A Positive'), ('AB+', 'AB Positive'), ('A-', 'A Neagtive'), ('B-', 'B Negative'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')])),
                ('student_phone_num', models.CharField(max_length=20)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_optional_phone_num', models.CharField(max_length=20, null=True, blank=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('parent_email', models.EmailField(max_length=254)),
                ('parent_phone_num', models.CharField(max_length=20)),
<<<<<<< HEAD
                ('parent_optional_phone_num', models.CharField(blank=True, null=True, max_length=20)),
                ('permanent_address', models.CharField(max_length=200)),
                ('permanent_address_zipcode', models.IntegerField(blank=True, null=True)),
                ('local_guardian_name', models.CharField(default='', max_length=100)),
                ('local_guardian_address', models.CharField(default='', max_length=200)),
                ('local_guardian_address_zipcode', models.IntegerField(default=0)),
                ('local_guardian_phone_num', models.CharField(default='', max_length=20)),
                ('local_guardian_optional_phone_num', models.CharField(default='', blank=True, max_length=20)),
                ('local_guardian_email', models.EmailField(default='', max_length=254)),
                ('student_photo', models.ImageField(upload_to=newapp.models.student_photo_name, blank=True, null=True)),
=======
                ('parent_optional_phone_num', models.CharField(max_length=20, null=True, blank=True)),
                ('permanent_address', models.CharField(max_length=200)),
                ('permanent_address_zipcode', models.IntegerField(null=True, blank=True)),
                ('local_guardian_name', models.CharField(max_length=100, default='')),
                ('local_guardian_address', models.CharField(max_length=200, default='')),
                ('local_guardian_address_zipcode', models.IntegerField(default=0)),
                ('local_guardian_phone_num', models.CharField(max_length=20, default='')),
                ('local_guardian_optional_phone_num', models.CharField(max_length=20, default='', blank=True)),
                ('local_guardian_email', models.EmailField(max_length=254, default='')),
                ('student_photo', models.ImageField(upload_to=newapp.models.student_photo_name, null=True, blank=True)),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
                ('branch', models.ForeignKey(to='newapp.Branch')),
                ('room_number', models.ForeignKey(to='newapp.Rooms', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='previoushosteldetail',
            name='student',
<<<<<<< HEAD
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='newapp.Students'),
=======
            field=models.ForeignKey(to='newapp.Students', null=True, on_delete=django.db.models.deletion.SET_NULL),
>>>>>>> 1b5467dc77f5d6cc74c99ebaa4d092bef48c6baf
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
