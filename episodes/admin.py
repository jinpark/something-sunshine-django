from django.contrib import admin
from episodes.models import Episode, Tag

class EpisodeAdmin(admin.ModelAdmin):
	readonly_fields = ('modified','created', 'file_size')
	list_display = ('number', 'title')

admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Tag)