from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache

from .forms import ProposalForm
from .models import Conference

def home(request):
    """the homepage - which redirects to the current Conference context"""
    conference =  get_object_or_404(Conference, active=True)
    return redirect(reverse('conference' , args=[conference.slug]))

def conference(request, slug):
    """the actual conference homepage"""
    articles = Article.objects.filter(published=True).order_by('-created_at').all()
    return render_to_response('home.html', {
        'articles': articles,
    }, RequestContext(request))

@never_cache # causes issues with reloading data from form
def submit(request, slug, proposal_id=None):
    """
    here the user can:
    a) register for an account, if the user has not already done so OR
    b) view talk submissions that user has submitted AND submit new talks
    
    """
    if not request.user.is_authenticated():
        request.session['next'] = request.path # redirect back here after signup
        return redirect(reverse('signup')) # redirect to signup page
    else:
        if proposal_id:
            proposal = get_object_or_404(request.user.proposals, conference=request.conference, id=proposal_id)
        else:
            proposal = None
        proposals = request.conference.proposals.filter(user=request.user)
        if request.method == 'POST':
            form = ProposalForm(request.POST, request=request, instance=proposal)
            if form.is_valid():
                form.save()
                return redirect(reverse('submit', args=[request.conference.slug]))
        else:
            form = ProposalForm(request=request, instance=proposal)
        return render_to_response('submit.html', {
            'form': form,
            'proposal': proposal,
            'proposals': proposals,
        }, RequestContext(request))
    