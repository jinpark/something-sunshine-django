# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0003_episode_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='file_size',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='episode',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
