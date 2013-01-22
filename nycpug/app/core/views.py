from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from app.core.models import Conference, Proposal, Room, Speaker, Schedule
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
    conference = Conference.objects.filter(active=True).latest('id')
    schedule = conference.schedule_set.order_by('start_time').all()
    rooms = Room.objects.filter(venue__conference__active=True).order_by('name').distinct().all()
    room_positions = [r for r in rooms]
    master_list = []
    current_time = None
    for item in schedule:
        if item.start_time != current_time:
            current_time = item.start_time
            master_list.append([item.start_time, item.end_time])
            if item.entire_space:
                master_list[-1].append([item])
            else:
                master_list[-1].append(list(range(len(room_positions))))
                master_list[-1][2][room_positions.index(item.room)] = item
        else:
            master_list[-1][2][room_positions.index(item.room)] = item
    return render_to_response('schedule.html', {
        'master_list': master_list,
        'room_positions': room_positions,
    }, RequestContext(request))

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

def talk(request, proposal_id):
    proposal = get_object_or_404(Proposal, accepted=True, id=proposal_id)
    return render_to_response('talk.html', {
        'proposal': proposal,
    }, RequestContext(request))