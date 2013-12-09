from django.contrib import admin

from .models import *

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'start_date', 'end_date', 'active',)
    list_filter = ('active',)
    filter_horizontal = ('sponsor_categories',)
    ordering = ['-start_date']

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'conference')
    list_filter = ('category', 'conference')
    search_fields = ('name', 'category__name', 'conference__name',)

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorCategory)
