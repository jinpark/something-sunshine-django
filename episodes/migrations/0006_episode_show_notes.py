# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0005_auto_20150523_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='show_notes',
            field=models.TextField(default='', help_text=b'Show notes here!'),
            preserve_default=False,
        ),
    ]
