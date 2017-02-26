# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0009_remove_computers_days_old'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputersAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('computer_name', models.CharField(max_length=30, null=True, blank=True)),
                ('IP_address', models.CharField(max_length=30, null=True, blank=True)),
                ('MAC_address', models.CharField(max_length=30, null=True, blank=True)),
                ('users_name', models.CharField(max_length=30, null=True, blank=True)),
                ('location', models.CharField(max_length=30, null=True, blank=True)),
                ('Unit', models.CharField(default=b'', max_length=50, null=True, blank=True, choices=[(b'Accounting Unit', b'Accounting Unit'), (b'Treasury Unit', b'Treasury Unit')])),
                ('added_by', models.CharField(max_length=30, null=True, blank=True)),
                ('edited_by', models.CharField(max_length=30, null=True, blank=True)),
                ('export_to_CSV', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Operating_system', models.ForeignKey(blank=True, to='djangoapp.OperatingSystem', null=True)),
            ],
        ),
    ]
