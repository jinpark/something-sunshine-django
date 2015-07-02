from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings

from urlparse import urlparse

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def xml_escape(string):
    """Replaces all unescaped xml characters"""
    return string.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')


@register.simple_tag
def static_url(url):
	""" returns the static url-ed version of the path, and not the s3 version """
	full_s3_path = urlparse(url).path
	relative_path = "/".join(full_s3_path.split('/')[2:])
	return u"{}{}".format(settings.STATIC_BUCKET_URL, relative_path)