# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0010_computersaudit'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='date_edited',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 23, 15, 4, 14, 687434, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computersaudit',
            name='date_edited',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 23, 15, 4, 29, 357369, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
