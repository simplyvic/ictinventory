# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_auto_20161116_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='computers',
            name='Unit',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, choices=[(b'Accounting Unit', b'Accounting Unit'), (b'Treasury Unit', b'Treasury Unit')]),
        ),
    ]
