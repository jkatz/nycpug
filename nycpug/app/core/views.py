from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from app.core.models import Conference, Room, Speaker, Schedule
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

def schedule(request):
    schedule = Schedule.objects.order_by('start_time').all()
    rooms = Room.objects.filter(venue__conference__active=True).order_by('name').distinct().all()
    room_positions = [r for r in rooms]
    master_list = []
    current_time = None
    for item in schedule:
        if item.start_time != current_time:
            current_time = item.start_time
            master_list.append([item.start_time, item.end_time, [item]])
        else:
            master_list[-1][2].append(item)
    return render_to_response('schedule.html', {
        'master_list': master_list,
        'room_positions': room_positions,
    }, RequestContext(request))

def speakers(request):
    speakers = Speaker.objects.filter(proposals__accepted=True).order_by('name').distinct()
    return render_to_response('speakers.html', {
        'speakers': speakers,
    }, RequestContext(request))