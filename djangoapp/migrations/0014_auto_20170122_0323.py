# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0013_auto_20170122_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='date_edited',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='computersaudit',
            name='date_edited',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
