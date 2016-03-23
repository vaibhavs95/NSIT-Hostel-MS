# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import newapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20160324_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilities',
            name='photo',
            field=models.ImageField(upload_to=newapp.models.facility_photo_name, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 23, 19, 18, 6, 532802, tzinfo=utc)),
        ),
    ]
