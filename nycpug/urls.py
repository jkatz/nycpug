from django.conf import settings
from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'nycpug.app.core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'nycpug.app.account.views.login', name='login'),
    url(r'^logout/$', 'nycpug.app.account.views.logout', name='logout'),
    url(r'^reset_password/$', 'django.contrib.auth.views.password_reset', {},
        name='password_reset',
    ),
    url(r'^reset_password/done/$', 'django.contrib.auth.views.password_reset_done', {},
        name='password_reset_done',
    ),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {},
        name='password_reset_confirm',
    ),
    url(r'^reset_password/complete/$', 'django.contrib.auth.views.password_reset_complete', {},
        name='password_reset_complete',
    ),
    url(r'^signup/$', 'nycpug.app.account.views.signup', name='signup'),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^(?P<slug>[0-9]{4})/', include('nycpug.app.core.urls')),
    # url(r'^speakers/', 'app.core.views.speakers', name='speakers'),
    # url(r'^talk/(?P<proposal_id>\d+)', 'app.core.views.talk', name='talk'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }))
