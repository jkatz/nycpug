from django.contrib import admin

from models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'published',)
    ordering = ['-created_at']

admin.site.register(Article, ArticleAdmin)