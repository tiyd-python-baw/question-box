# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='voter',
            field=models.ForeignKey(related_name='voter', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='answers',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 19, 12, 58, 804771)),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 19, 12, 58, 804110)),
        ),
    ]
