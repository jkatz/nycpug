import re
from nycpug.app.core.models import Conference

class ConferenceMiddleware(object):
    """sets "request.conference" attribute based on the path"""

    def process_request(self, request):
        # don't do any redirect if we don't match anything - user might be going to the admin on initial load
        if request.path: # if there is a path we can set this
            parts = request.path.split('/')
            if parts[1] and re.match(r'[0-9]{4}', parts[1]):
                try:
                    request.conference = Conference.objects.get(slug=parts[1])
                except Conference.DoesNotExist:
                    try:
                        request.conference = Conference.objects.filter(active=True).latest('id')
                    except Conference.DoesNotExist:
                        pass
            else:
                try:
                    request.conference = Conference.objects.filter(active=True).latest('id')
                except Conference.DoesNotExist:
                    pass
        else:
            try:
                request.conference = Conference.objects.filter(active=True).latest('id')
            except Conference.DoesNotExist:
                pass
