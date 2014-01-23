from django.conf.urls import *

urlpatterns = patterns('nycpug.app.core.views',
    url(r'^$', 'conference', name='conference'),
    url(r'^event/(?P<event_id>\d+)/$', 'speaker', name='speaker'),
    url(r'^schedule/', 'schedule', name='schedule'),
    url(r'^submit/(?P<proposal_id>(\d+))?$', 'submit', name='submit'),
)