# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0002_auto_20150411_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='number',
            field=models.PositiveIntegerField(default=1, help_text=b'The episode number'),
        ),
    ]
