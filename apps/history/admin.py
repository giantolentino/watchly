from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "media_type", "date_added")


admin.site.register(Entry, EntryAdmin)
