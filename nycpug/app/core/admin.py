from django.contrib import admin

from .models import *

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
    list_display = ('event_title', 'event_speaker',)

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'conference')
    search_fields = ('title', 'user__name',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue',)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'conference')
    list_filter = ('category', 'conference')
    search_fields = ('name', 'category__name', 'conference__name',)

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
admin.site.register(Venue, VenueAdmin)
