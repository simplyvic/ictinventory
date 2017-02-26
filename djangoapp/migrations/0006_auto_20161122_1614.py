# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_auto_20161118_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='added_by',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='computers',
            name='edited_by',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
