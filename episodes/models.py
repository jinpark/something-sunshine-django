from django.db import models
from django.utils import timezone
from s3direct.fields import S3DirectField
import requests
import datetime

class Episode(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    audio_file_path = S3DirectField(dest='episode_audio')
    thumbnail = S3DirectField(dest='episode_thumbnail')
    description = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    number = models.PositiveIntegerField(default=1, help_text="The episode number")
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    duration = models.CharField(blank=False, max_length=8, default='00:00', help_text='Duration of the audio file, in MM:SS or HH:MM:SS format')
    file_size = models.PositiveIntegerField()
    show_notes = models.TextField(help_text="Show notes here!")

    def __unicode__(self):
        return u'{}'.format(self.title)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps and file size'''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        if self.audio_file_path:
            # bleh, this is a bad way to do this
            r = requests.head(self.audio_file_path)
            self.file_size = float(r.headers['content-length'])
        return super(Episode, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)


class Tag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False)
    image_file = S3DirectField(dest='tag_image')
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return u'{}'.format(self.name)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Tag, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)