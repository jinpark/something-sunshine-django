# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0004_auto_20150522_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='file_size',
            field=models.PositiveIntegerField(),
        ),
    ]
