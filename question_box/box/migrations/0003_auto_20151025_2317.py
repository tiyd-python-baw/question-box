# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0002_auto_20151025_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 23, 17, 5, 738779)),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 23, 17, 5, 737599)),
        ),
    ]
