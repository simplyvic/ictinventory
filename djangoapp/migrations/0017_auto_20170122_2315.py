# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0016_auto_20170122_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computers',
            name='leave_periods',
        ),
        migrations.AlterField(
            model_name='computers',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='computersaudit',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
    ]
