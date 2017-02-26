# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 14, 16, 11, 40, 21978, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
