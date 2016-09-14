from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Article(models.Model):
    """news about the conference that goes on the main page"""
    conference = models.ForeignKey('Conference', related_name='articles')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

class Block(models.Model):
    """block out a time period during the conference for a series of Events"""
    day = models.ForeignKey('Day', related_name='blocks')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return "%s %s-%s" % (self.day, self.start_time, self.end_time)

    class Meta:
        ordering = ['day__event_date', 'start_time']

class Conference(models.Model):
    """the big one - stores overall conference information"""
    name = models.TextField()
    slug = models.SlugField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)
    is_call_for_papers_active = models.BooleanField(default=False)
    is_schedule_active = models.BooleanField(default=False)

    sponsor_categories = models.ManyToManyField('SponsorCategory', blank=True, related_name='conferences')

    def set_active(self):
        """can only have one active Conference"""
        queryset = Conference.objects.filter(active=True)
        if self.id:
            queryset.exclude(id=self.id)
        if queryset.exists():
            if self.active:
                queryset.update(active=False)
            elif not self.active and queryset.filter(id=self.id).exists():
                self.active = True
        else:
            self.active = True

    def __unicode__(self):
        return self.name

class Day(models.Model):
    """used to organize a schedule for a given day for a Conference / Venue pair"""
    conference = models.ForeignKey('Conference', related_name='days')
    venue = models.ForeignKey('Venue', related_name='days')
    event_date = models.DateField()
    subtitle = models.TextField(null=True, blank=True)
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        title = self.event_date.strftime('%m-%d-%Y')
        if self.subtitle:
            title += ' - ' + self.subtitle
        return title

    class Meta:
        ordering = ['event_date', 'sort_order']

class Event(models.Model):
    """
    keeps information for an Event in the Conference
    if Proposal is assigned, then keeps info in sync from the Proposal
    """
    block = models.ForeignKey('Block', related_name='events')
    room = models.ForeignKey('Room', related_name='events')
    proposal = models.OneToOneField('Proposal', null=True, blank=True)
    track = models.ForeignKey('Track', null=True, blank=True)
    event_title = models.CharField(max_length=255, blank=True, help_text='Name of the Event')
    event_speaker = models.CharField(max_length=255, blank=True, help_text='Who is running the event')
    event_description = models.TextField(blank=True, help_text='Longer description of what the event is')
    event_bio = models.TextField(blank=True, help_text='Description of the speaker')
    is_full_block = models.BooleanField(default=False, help_text='Check this if this is the only event in the block')
    slug = models.SlugField(blank=True, null=True, max_length=1024)

    def sync_with_models(self):
        """if an Event is associated with this instance, update the info"""
        # only perform this action if Event is new
        if self.id is None and self.proposal:
            try:
                self.event_title = self.proposal.title
                self.slug = slugify(self.event_title)
                self.event_speaker = self.proposal.user.get_full_name()
                self.event_description = self.proposal.description
                self.event_bio = self.proposal.user.profile.description
            except Proposal.DoesNotExist:
                pass

    def __unicode__(self):
        return self.event_title

class Opinion(models.Model):
    """an opinion on a talk proposal"""
    user = models.ForeignKey('account.User', related_name='opinions') # user who has the opinion
    proposal = models.ForeignKey('core.Proposal', related_name='opinions')
    is_recommended = models.BooleanField(default=False)
    description = models.TextField() # the description of the opinion
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'proposal'),)
        permissions = (
            ('create_opinion', 'User can create proposal opinions'),
        )

class Proposal(models.Model):
    """
    contains the proposal information submitted by account.User for
    core.Conference
    """
    FORMATS = (
        # ('Regular', '50-Min Session (Apr 19 - 20)',),
        # ('Training', '3-Hour Training (Apr 18)',),
        # ('Summit', 'Regulated Industry Summit (Apr 18)',),
        ('2016-session', '50-Min Session (Mar 29 - 31)',),
        ('2016-training', '3-Hour Training (Mar 18)',),
        ('2016-ris', 'Regulated Industry Summit (Mar 28)',),
    )
    STATUS = (
        ('', 'Undecided'),
        ('declined', 'Declined'),
        ('accepted', 'Accepted'),
    )
    conference = models.ForeignKey('Conference', related_name='proposals')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='proposals')
    title = models.CharField(max_length=255)
    format = models.CharField(max_length=255, null=True, blank=True, choices=FORMATS, default='Regular')
    description = models.TextField()
    other = models.TextField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    status = models.CharField(max_length=255, null=True, blank=True, choices=STATUS, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def format_title(self):
        """returns the format in titleized form"""
        for format_type in self.FORMATS:
            if format_type[0] == self.format:
                return format_type[1]

    def status_title(self):
        """returns the status in titleized form"""
        for status_tuple in self.STATUS:
            if status_tuple[0] == self.status:
                return status_tuple[1]

    def sync_with_models(self):
        """if an Event is associated with this instance, update the info"""
        # only perform this action if Proposal has already been created
        if self.id:
            try:
                self.event.event_title = self.title
                self.event.event_speaker = self.user.get_full_name()
                self.event.event_description = self.description
                self.event.save()
            except Event.DoesNotExist:
                pass

    def __unicode__(self):
        return self.title

class Room(models.Model):
    """entry for a room in a Venue"""
    venue = models.ForeignKey('Venue', related_name='rooms')
    name = models.TextField()
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Sponsor(models.Model):
    """core info for a Sponsor specific to a Conference"""
    conference = models.ForeignKey('Conference', related_name='sponsors')
    category = models.ForeignKey('SponsorCategory', related_name='sponsors')
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='sponsors/')
    url = models.URLField()
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']

class SponsorCategory(models.Model):
    """category to group sponsors"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    sort_order = models.IntegerField(default=0)
    css_class = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']
        verbose_name_plural =  'sponsor categories'

class Track(models.Model):
    """track and color-coding"""
    conference = models.ForeignKey('Conference', related_name='tracks')
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, help_text='Hex Code e.g. "#ffaa00"')

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.conference)

    class Meta:
        ordering = ['name']

class Venue(models.Model):
    """venue information for a Conference"""
    conference = models.ForeignKey('Conference', related_name='venues')
    sort_order = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=2)
    description = models.TextField()

    def __unicode__(self):
        return self.name

def set_active(sender, instance, *args, **kwargs):
    instance.set_active()

def sync_with_models(sender, instance, *args, **kwargs):
    instance.sync_with_models()

pre_save.connect(set_active, sender=Conference)
pre_save.connect(sync_with_models, sender=Event)
pre_save.connect(sync_with_models, sender=Proposal)
