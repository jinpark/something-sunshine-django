from django.conf.urls import patterns, url
from episodes import views

urlpatterns = patterns('',
    url(r'^$', views.homepage),
    url(r'^feed.xml/', views.feed),
    url(r'^newhome', views.newhome),
    url(r'^embed/(?P<id>[0-9])/$', views.embed),
)
