# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import newapp.models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_auto_20160327_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessDetail',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('wd_bf', models.TimeField()),
                ('wd_l', models.TimeField()),
                ('wd_s', models.TimeField()),
                ('wd_d', models.TimeField()),
                ('we_bf', models.TimeField()),
                ('we_l', models.TimeField()),
                ('we_s', models.TimeField()),
                ('we_d', models.TimeField()),
                ('wd_bf_c', models.TimeField()),
                ('wd_l_c', models.TimeField()),
                ('wd_s_c', models.TimeField()),
                ('wd_d_c', models.TimeField()),
                ('we_bf_c', models.TimeField()),
                ('we_l_c', models.TimeField()),
                ('we_s_c', models.TimeField()),
                ('we_d_c', models.TimeField()),
                ('menu', models.FileField(upload_to=newapp.models.messmenu_file_name)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 26, 20, 43, 57, 593937, tzinfo=utc)),
        ),
    ]
