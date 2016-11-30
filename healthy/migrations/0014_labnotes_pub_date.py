# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-30 21:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('healthy', '0013_labnotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='labnotes',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 30, 21, 19, 50, 954469, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
