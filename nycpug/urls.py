from django.conf import settings
from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'nycpug.app.core.views.home', name='home'),
    url(r'^account/', include('nycpug.app.account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'nycpug.app.account.views.login', name='login'),
    url(r'^logout/$', 'nycpug.app.account.views.logout', name='logout'),
    url(r'^signup/$', 'nycpug.app.account.views.signup', name='signup'),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^(?P<slug>[0-9]{4})/', include('nycpug.app.core.urls')),
    # url(r'^registration/', 'app.core.views.registration', name='registration'),
    # url(r'^schedule/', 'app.core.views.schedule', name='schedule'),
    # url(r'^speakers/', 'app.core.views.speakers', name='speakers'),
    # url(r'^talk/(?P<proposal_id>\d+)', 'app.core.views.talk', name='talk'),
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }))