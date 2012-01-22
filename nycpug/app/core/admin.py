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
        models.TextField: { 'widget': AdminTinyMCE },
    }

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/tiny_mce/tiny_mce_popup.js',)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Conference, ConferenceAdmin)