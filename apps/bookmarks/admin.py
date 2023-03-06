from django.contrib import admin
from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("title", "media_type", "priority", "date_added")


admin.site.register(Bookmark, BookmarkAdmin)
