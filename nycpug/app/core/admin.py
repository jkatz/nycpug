from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.db import models

from tinymce.widgets import AdminTinyMCE

from app.core.models import *

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'active',)
    filter_horizontal = ('sponsor_categories',)
    ordering = ['-start_date']

class FlatPageAdmin(FlatPageAdminOld):
    formfield_overrides = {
        models.TextField: {
            'widget': AdminTinyMCE()
        },
    }

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/tiny_mce/tiny_mce_popup.js',)

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'proposal_name', 'conference', )

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue',)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'proposal', 'title')

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Speaker)
admin.site.register(Venue)