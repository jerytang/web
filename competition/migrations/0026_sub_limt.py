# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-12 08:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competition', '0025_auto_20170312_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_limt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_valid', models.BooleanField(default=False)),
                ('is_final', models.BooleanField(default=False)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.Competition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
