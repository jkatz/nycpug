from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from nycpug.app.core.models import Conference

def home(request):
    """the homepage - which redirects to the current Conference context"""
    conference =  get_object_or_404(Conference, active=True)
    return redirect(reverse('conference' , args=[conference.slug]))

def conference(request, slug):
    """the actual conference homepage"""
    conference = get_object_or_404(Conference, slug=slug)
    # articles = Article.objects.filter(published=True).order_by('-created_at').all()
    return render_to_response('home.html', {
        # 'articles': articles,
        'conference': conference,
    }, RequestContext(request))
