# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 22, 53, 16, 349145)),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 22, 53, 16, 347950)),
        ),
    ]
