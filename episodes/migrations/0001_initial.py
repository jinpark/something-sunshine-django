# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('audio_file_path', s3direct.fields.S3DirectField()),
                ('thumbnail', s3direct.fields.S3DirectField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('image_file', s3direct.fields.S3DirectField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='episode',
            name='tags',
            field=models.ManyToManyField(to='episodes.Tag', blank=True),
        ),
    ]
