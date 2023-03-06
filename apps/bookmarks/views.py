from django.views.generic import ListView
from .models import Bookmark


# Create your views here.
class BookmarksView(ListView):
    model = Bookmark
    context_object_name = "entries"
    template_name = "bookmarks/bookmarks.html"
