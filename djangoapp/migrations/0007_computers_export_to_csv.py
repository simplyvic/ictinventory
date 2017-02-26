# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0006_auto_20161122_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
    ]
