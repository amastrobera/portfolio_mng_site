# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 19:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_mng_app', '0004_auto_20160326_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 26, 19, 6, 0, 798897, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='last_update_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 26, 19, 6, 0, 798941, tzinfo=utc)),
        ),
    ]
