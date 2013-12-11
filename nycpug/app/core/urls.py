from django.conf.urls import *

urlpatterns = patterns('nycpug.app.core.views',
    url(r'^$', 'conference', name='conference'),
    url(r'^schedule/', 'app.core.views.schedule', name='schedule'),
    url(r'^submit/(?P<proposal_id>(\d+))?$', 'submit', name='submit'),
)