from nycpug.app.core.models import Conference

def conference(request):
    """always have access to the conference, everywhere"""
    return { 'conference': request.conference }

def sponsors(request):
    """returns grouped list of all core.Sponsor objects, grouped by sponsor.Category"""
    try:
        conference = request.conference
        sponsors = []
        for category in conference.sponsor_categories.all():
            sponsors.append({
                'category': category.name,
                'sponsors': [sponsor for sponsor in conference.sponsors.filter(category=category).all()]
            })
    except Conference.DoesNotExist:
        return {}
    return { 'sponsors': sponsors }
