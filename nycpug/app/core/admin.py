from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'conference', 'user', 'created_at', 'published',)
    ordering = ['-created_at']

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'start_date', 'end_date', 'active',)
    list_filter = ('active',)
    filter_horizontal = ('sponsor_categories',)
    ordering = ['-start_date']

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'conference')
    list_filter = ('conference')
    search_fields = ('title', 'user__name',)


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'conference')
    list_filter = ('category', 'conference')
    search_fields = ('name', 'category__name', 'conference__name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorCategory)
