# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_computers_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='IP_address',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='computers',
            name='MAC_address',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='computers',
            name='computer_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='computers',
            name='location',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='computers',
            name='users_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
