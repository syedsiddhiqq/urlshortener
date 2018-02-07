from django.conf.urls import url
from .views import wildcard_redirect
urlpatterns = [
    url(r'^(?P<path>.*)', wildcard_redirect),
    #url(r'^a/(?P<shortcode>[\w-]+){6,15}/$',falcomx_redirect_views),
]
