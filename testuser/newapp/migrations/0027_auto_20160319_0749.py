# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0026_auto_20160316_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostels',
            old_name='warden_department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='hostels',
            old_name='warden_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='hostels',
            old_name='warden_landLine',
            new_name='landline',
        ),
        migrations.RenameField(
            model_name='hostels',
            old_name='warden_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='hostels',
            old_name='warden_phone_num',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='hostels',
            old_name='warden_portfolio',
            new_name='portfolio',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 19, 7, 49, 2, 726461, tzinfo=utc)),
        ),
    ]
