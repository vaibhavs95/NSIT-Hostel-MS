# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import newapp.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20160326_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200, default='')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=newapp.models.form_file_name)),
                ('hostel', models.ForeignKey(to='newapp.Hostels')),
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 26, 20, 11, 46, 603970, tzinfo=utc)),
        ),
    ]
