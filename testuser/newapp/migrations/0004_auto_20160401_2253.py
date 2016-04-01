# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import newapp.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20160401_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminalrecord',
            name='file',
            field=models.FileField(null=True, upload_to=newapp.models.CriminalRecordFile),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 4, 1, 17, 23, 27, 916383, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='previoushosteldetail',
            name='hostel_name',
            field=models.CharField(max_length=40),
        ),
    ]
