from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    #host(r'blog','falcomx.hostsconf.urls',name='blog')
    host(r'(?!www).*', 'falcomx.hostsconf.urls', name='wildcard'),
)
