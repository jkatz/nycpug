from django.contrib import admin

from nycpug.app.core.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'conference', 'user', 'created_at', 'published',)
    ordering = ['-created_at']

class BlockAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time',)

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'start_date', 'end_date', 'active',)
    list_filter = ('active',)
    filter_horizontal = ('sponsor_categories',)
    ordering = ['-start_date']

class DayAdmin(admin.ModelAdmin):
    list_display = ('event_date', 'venue', 'conference',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_speaker', 'conference_name',)
    list_filter = ('block__day__conference',)

    def conference_name(self, obj):
        return obj.block.day.conference.name

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'block':
            kwargs['queryset'] = Block.objects.filter(day__conference__active=True).order_by('day__event_date', 'start_time').all()
        elif db_field.name == 'room':
            kwargs['queryset'] = Room.objects.filter(venue__conference__active=True).order_by('sort_order').all()
        elif db_field.name == 'proposal':
            kwargs['queryset'] = Proposal.objects.filter(conference__active=True, status='accepted').order_by('title').all()
        elif db_field.name == 'track':
            kwargs['queryset'] = Track.objects.filter(conference__active=True).order_by('name').all()
        return super(EventAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'conference', 'format', 'status',)
    list_filter = ('conference', 'format', 'status',)
    search_fields = ('title', 'user__name',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue',)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'conference')
    list_filter = ('category', 'conference')
    search_fields = ('name', 'category__name', 'conference__name',)

class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'conference', 'color',)
    ordering = ['conference']

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'city', 'state', 'zip', 'conference',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorCategory)
admin.site.register(Track, TrackAdmin)
admin.site.register(Venue, VenueAdmin)
