# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-17 13:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0006_auto_20160504_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='final_submit_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 17, 13, 25, 38, 558369, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
