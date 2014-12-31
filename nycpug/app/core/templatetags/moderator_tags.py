import re
from django import template
from django.template.defaultfilters import stringfilter
from django.template.loader import render_to_string
from nycpug.app.core.models import Room

register = template.Library()

@register.simple_tag
def did_i_review(proposal, user):
    """returns YES or NO based on if user reviewed proposals"""
    if proposal.opinions.filter(user=user).exists():
        return '<strong style="color:green">YES</strong>'
    else:
        return '<strong style="color:red">NO</strong>'

@register.simple_tag
def total_positive_opinions(proposal):
    """returns a count of total positive opinions"""
    return proposal.opinions.filter(is_recommended=True).count()
