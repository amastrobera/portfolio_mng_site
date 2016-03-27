# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 16:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_mng_app', '0015_auto_20160327_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 27, 16, 30, 57, 890517, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='last_update_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 27, 16, 30, 57, 890570, tzinfo=utc)),
        ),
    ]
