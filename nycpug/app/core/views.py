from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from app.core.models import Conference, Speaker
from app.core.forms import ProposalForm
from app.news.models import Article

def home(request):
    articles = Article.objects.filter(published=True).order_by('-created_at').all()
    try:
        conference = Conference.objects.filter(active=True).order_by('start_date').all()[0]
    except IndexError:
        conference = None
    return render_to_response('home.html', {
        'articles': articles,
        'conference': conference,
    }, RequestContext(request))

def registration(request):
    return render_to_response('registration.html', {}, RequestContext(request))

def speakers(request):
    speakers = Speaker.objects.filter(proposals__accepted=True).order_by('name').distinct()
    return render_to_response('speakers.html', {
        'speakers': speakers,
    }, RequestContext(request))