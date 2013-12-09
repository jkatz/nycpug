from django.conf.urls import *

urlpatterns = patterns('nycpug.app.core.views',
    url(r'^$', 'conference', name='conference'),
)