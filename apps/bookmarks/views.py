from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
class BookmarksView(ListView):
    model = Bookmark
    context_object_name = "entries"
    template_name = "bookmarks/index.html"


class BookmarkDetailView(DetailView):
    model = Bookmark
    template_name = "bookmarks/detailed.html"
    context_object_name = "entry"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def delete_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    bookmark.delete()
    return redirect("bookmarks:index")
