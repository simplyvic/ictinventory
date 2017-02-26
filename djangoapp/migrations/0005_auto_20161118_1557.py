# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0004_computers_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Operating_system', models.CharField(default=b'', max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='computers',
            name='Operating_system',
            field=models.ForeignKey(blank=True, to='djangoapp.OperatingSystem', null=True),
        ),
    ]
