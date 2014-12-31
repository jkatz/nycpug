from django.conf.urls import *

from .views import *

urlpatterns = patterns('nycpug.app.core.admin.views',
    url(r'^conference/(?P<slug>[0-9]{4})/$', ConferenceView.as_view(), name='admin_moderate_conference'), # view overall conference stats
    url(r'^conference/(?P<slug>[0-9]{4})/proposal/(?P<proposal_id>\d+)/$', ProposalView.as_view(), name='admin_moderate_conference_proposal'), # view a proposal
    url(r'^dashboard/$', DashboardView.as_view(), name='admin_moderate'), # index, can't have '' index because of Django admin
)
