from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from app.core.models import Conference
from app.news.models import Article

def home(request):
    articles = Article.objects.filter(published=True).order_by('-created_at').all()
    try:
        conference = Conference.objects.filter(active=True).order_by('start_date').all()[0]
        sponsors = []
        for category in conference.sponsor_categories.all():
            sponsors.append({
                'category': category.name,
                'sponsors': [sponsor for sponsor in conference.sponsors.filter(category=category).all()]
            })
    except IndexError:
        conference = None
        sponsors = None
    print sponsors
    return render_to_response('home.html', {
        'articles': articles,
        'conference': conference,
        'sponsors': sponsors,
    }, RequestContext(request))