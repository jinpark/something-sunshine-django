# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='duration',
            field=models.CharField(default=b'00:00', help_text=b'Duration of the audio file, in MM:SS or HH:MM:SS format', max_length=8),
        ),
        migrations.AddField(
            model_name='episode',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tag',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='episode',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
