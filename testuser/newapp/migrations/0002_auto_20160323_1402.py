# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import newapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostels',
            name='warden_photo',
            field=models.ImageField(null=True, upload_to=newapp.models.warden_photo_name, blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 23, 8, 32, 45, 942285, tzinfo=utc)),
        ),
    ]
