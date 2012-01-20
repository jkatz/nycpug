from django.contrib import admin

from models import *

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'conference', 'category')

class SponsorCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = { 'slug': ('name',) }

admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorCategory, SponsorCategoryAdmin)
