# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0011_auto_20161123_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='leave_periods',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
