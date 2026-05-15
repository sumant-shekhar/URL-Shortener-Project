from django.contrib import admin
from .models import URL

# Register your models here.
class URLAdmin(admin.ModelAdmin):
    list_display = ('url', 'uuid')
    search_fields = ('url', 'uuid')
admin.site.register(URL, URLAdmin)