# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0014_auto_20170122_0323'),
    ]

    operations = [
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
