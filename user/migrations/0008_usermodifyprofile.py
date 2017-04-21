# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-30 10:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0007_userinfo_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModifyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=30)),
                ('modify_datetime', models.DateTimeField()),
                ('mod_before', models.TextField(blank=True, max_length=500)),
                ('mode_after', models.TextField(blank=True, max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]