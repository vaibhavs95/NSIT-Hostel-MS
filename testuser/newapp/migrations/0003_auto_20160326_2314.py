# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import newapp.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20160326_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostelcouncil',
            old_name='dept',
            new_name='dept_or_room',
        ),
        migrations.RemoveField(
            model_name='hostelcouncil',
            name='member',
        ),
        migrations.RemoveField(
            model_name='hostelcouncil',
            name='room_no',
        ),
        migrations.AddField(
            model_name='hostelcouncil',
            name='photo',
            field=models.ImageField(upload_to=newapp.models.council_photo_name, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 26, 17, 44, 3, 541951, tzinfo=utc)),
        ),
    ]
