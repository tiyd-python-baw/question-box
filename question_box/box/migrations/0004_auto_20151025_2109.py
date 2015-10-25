# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('box', '0003_auto_20151025_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 9, 18, 24894)),
        ),
        migrations.RemoveField(
            model_name='answers',
            name='voter',
        ),
        migrations.AddField(
            model_name='answers',
            name='voter',
            field=models.ForeignKey(related_name='voter', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 9, 18, 24211)),
        ),
    ]
