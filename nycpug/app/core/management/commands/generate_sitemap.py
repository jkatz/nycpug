import sys

from lxml import etree
from lxml.builder import E

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.urlresolvers import reverse

from nycpug.app.core.models import Conference, Event

class Command(BaseCommand):
    help = 'generates a sitemap, used primarily by google sitemaps'
    SITE_URL = 'http://www.pgconf.us'

    def handle(self, *args, **options):
        events = []
        for event in Event.objects.order_by('-block__day__conference__slug'):
            events.extend(
                E.url(
                    E.loc('%s%s' % (self.SITE_URL, reverse('speaker_with_slug', args=[event.block.day.conference.slug, event.id, event.slug]),)),
                    E.changefreq('weekly'),
                )
            )
        for conference in Conference.objects.all():
            events.extend(
                [
                    E.url(
                        E.loc('%s/%s' % (self.SITE_URL, conference.slug)),
                        E.changefreq('weekly'),
                    ),
                    E.url(
                        E.loc('%s/%s/schedule/' % (self.SITE_URL, conference.slug)),
                        E.changefreq('monthly'),
                    ),
                    E.url(
                        E.loc('%s/%s/tickets/' % (self.SITE_URL, conference.slug)),
                        E.changefreq('monthly'),
                    ),
                    E.url(
                        E.loc('%s/%s/sponsor/' % (self.SITE_URL, conference.slug)),
                        E.changefreq('monthly'),
                    ),
                ]
            )
        xml = E.urlset({'xmlns':'http://www.sitemaps.org/schemas/sitemap/0.9'}, *events)
        f = open(settings.SITEMAP_PATH, 'w')
        f.write("""<?xml version="1.0" encoding="UTF-8"?>\n""")
        f.write(etree.tostring(xml, pretty_print=True))
        f.close()
