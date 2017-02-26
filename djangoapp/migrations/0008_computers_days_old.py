# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0007_computers_export_to_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='days_old',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
