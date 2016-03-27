# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelCouncil',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=15)),
                ('position', models.CharField(default='', max_length=100)),
                ('member', models.CharField(choices=[('F', 'Faculty'), ('S', 'Student')], default='F', max_length=15)),
                ('committee', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('dept', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('room_no', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 26, 17, 37, 16, 829414, tzinfo=utc)),
        ),
    ]
