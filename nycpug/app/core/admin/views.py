# nycpug.app.core.admin.views
# special file to handle admin based moderation views

from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic.base import TemplateView, View

from nycpug.app.core.models import *

from .forms import *

__all__ = [
    'ConferenceView',
    'DashboardView',
    'ProposalView',
]

# access mixins
class ModeratorMixin(View):
    """restrict access to just admins"""
    @method_decorator(never_cache)
    @method_decorator(user_passes_test(lambda user: user.has_perm('core.create_opinion')))
    def dispatch(self, *args, **kwargs):
        return super(ModeratorMixin, self).dispatch(*args, **kwargs)

# views

class ConferenceView(TemplateView, ModeratorMixin):
    """index page for moderating a conference"""
    template_name = 'admin/moderate/conference.html'

    def get_context_data(self, slug, *args, **kwargs):
        context = super(ConferenceView, self).get_context_data(*args, **kwargs)
        context['conference'] = conference = get_object_or_404(Conference.objects, slug=slug)
        context['stats'] = {
            'total_user_opinions': Opinion.objects.filter(proposal__conference=conference, user=self.request.user).count(),
            'total_user_recommendations': Opinion.objects.filter(proposal__conference=conference, user=self.request.user, is_recommended=True).count(),
            'total_opinions': Opinion.objects.filter(proposal__conference=conference).count(),
            'accepted_proposals': conference.proposals.filter(status='accepted').count(),
            'declined_proposals': conference.proposals.filter(status='declined').count(),
            'total_proposals': conference.proposals.count(),
        }
        context['stats']['undecided_proposals'] = context['stats']['total_proposals'] - context['stats']['accepted_proposals'] - context['stats']['declined_proposals']
        # works due to unique constraint
        context['stats']['total_user_need_opinions'] = context['stats']['total_proposals'] - context['stats']['total_user_opinions']
        # proposals
        context['proposals'] = Proposal.objects.raw("""SELECT p.*
        FROM core_proposal p
        LEFT OUTER JOIN core_opinion o ON
            o.proposal_id = p.id AND
            o.user_id = %(user_id)s
        WHERE p.conference_id = %(conference_id)s
        ORDER BY (o.id IS NOT NULL), p.created_at
        """, { 'user_id': self.request.user.id, 'conference_id': conference.id })
        return context

class DashboardView(TemplateView, ModeratorMixin):
    """index page for the moderation section"""
    template_name = 'admin/moderate/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context['conferences'] = Conference.objects.filter(active=True).order_by('start_date').all()
        return context

class ProposalView(ModeratorMixin):
    """page for moderating a proposal"""
    form_class = OpinionForm
    template_name = 'admin/moderate/proposal.html'

    def get(self, request, slug, proposal_id, *args, **kwargs):
        """view the proposal and opinions"""
        context = self._setup_context(request, slug, proposal_id)
        return render_to_response(self.template_name, context, RequestContext(request))

    def post(self, request, slug, proposal_id,*args, **kwargs):
        """view the proposal and opinions"""
        context = self._setup_context(request, slug, proposal_id)
        # validate the form
        if context.get('form').is_valid():
            context.get('form').save()
            return redirect(reverse('admin_moderate_conference', args=[slug]))
        # show form errors here
        return render_to_response(self.template_name, context, RequestContext(request))

    def _setup_context(self, request, slug, proposal_id):
        """return a dictionary that setups the request context"""
        context = {}
        context['conference'] = conference = get_object_or_404(Conference.objects, slug=slug)
        context['proposal'] = proposal = get_object_or_404(conference.proposals, id=proposal_id)
        context['opinions'] = proposal.opinions.order_by('-created_at').all()
        # setup form and instance (if it exists)
        try:
            opinion = context.get('opinions').get(user=request.user)
        except Opinion.DoesNotExist:
            opinion = Opinion()
        if request.POST:
            data = request.POST.copy()
            # force specific validation values
            data['user'] = request.user.id
            data['proposal'] = proposal.id
            data['is_recommended'] = True if request.POST.get('is_recommended') else False
            context['form'] = self.form_class(data, instance=opinion)
        else:
            context['form'] = self.form_class(instance=opinion)
        return context
