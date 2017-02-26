# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_computers_days_old'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computers',
            name='days_old',
        ),
    ]
