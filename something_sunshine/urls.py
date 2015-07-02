from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'something_sunshine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include('smuggler.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^s3direct/', include('s3direct.urls')),
    url(r'^', include('episodes.urls')),
)
