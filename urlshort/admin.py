from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("short_url", "original_url")
    search_fields = ("short_url", "original_url")