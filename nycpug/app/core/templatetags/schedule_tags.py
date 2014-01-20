from django import template
from django.template.loader import render_to_string
from nycpug.app.core.models import Room

register = template.Library()

@register.simple_tag
def render_schedule_for_day(day):
    """render a full schedule for a core.Day"""
    html = '<table border="1">\n'
    # first need to determine the overall order in which to render things
    # schedule_matrix = {}
    # schedule_matrix[day.id] = {
    #     'blocks': [],
    #     'rooms': [],
    # }
    rooms = []
    # line up the rooms...also had to deal with a weird Django issue hence the day__id
    for room in Room.objects.filter(events__block__day__id=day.id).distinct().order_by('name').all():
        rooms.append(room)
    # render the header row
    html += '  <thead>\n'
    html += '    ' + render_to_string('_schedule_header.html', { 'rooms': rooms })
    html += '  </thead>\n'
    html += '  <tbody>\n'
    for block in day.blocks.order_by('start_time').all(): # line up the blocks
        events = [None] * len(rooms)
        for event in block.events.all():
            if event.is_full_block:
                events[0] = event
            else:
                events[rooms.index(event.room)] = event
        html += '    ' + render_to_string('_schedule_row.html', {
            'rooms': rooms,
            'block': block,
            'events': events,
        })
    html += '  </tbody>\n'
    html += '</table>\n'
    return html
