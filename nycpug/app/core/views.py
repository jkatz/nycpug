from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from app.core.models import Conference
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
    message = None
    if request.POST:
        form = ProposalForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Thank you for your submission!  You may make more submissions using the form below.'
            form = ProposalForm(
                initial={
                    'name': form.cleaned_data.get('name'),
                    'email': form.cleaned_data.get('email'),
                }
            )
    else:
        form = ProposalForm()
    return render_to_response('speakers.html', {
        'form': form,
        'message': message,
    }, RequestContext(request))