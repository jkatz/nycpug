from django.contrib import admin

from models import *

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'active',)
    filter_horizontal = ('sponsor_categories',)
    ordering = ['-start_date']

admin.site.register(Conference, ConferenceAdmin)