from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.shortcuts import get_object_or_404, redirect
from .forms import UpdateBookmarkForm
from django.shortcuts import render
from apps.history.models import Entry
from datetime import date


class BookmarksView(ListView):
    model = Bookmark
    context_object_name = "entries"
    template_name = "bookmarks/index.html"

    def get_queryset(self):
        queryset = Bookmark.objects.filter(user=self.request.user).order_by(
            "-date_added"
        )
        sort = self.request.GET.get("sort_by")
        print(self.request.GET.get("sort_by"))
        queryset = sort_by(queryset, sort)
        return queryset


def sort_by(queryset, filter_by):
    ordering = {
        "1": "title",
        "2": "-title",
        "3": "-priority",
        "4": "priority",
        "5": "date_added",
        "6": "-date_added",
    }
    return queryset.order_by(ordering.get(filter_by, "-date_added"))


class BookmarkDetailView(DetailView):
    model = Bookmark
    template_name = "bookmarks/detailed.html"
    context_object_name = "entry"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UpdateBookmarkForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        bookmark = self.get_object()
        form = UpdateBookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return render(
                request, self.template_name, {"entry": bookmark, "form": form}
            )
        else:
            return render(
                request, self.template_name, {"entry": bookmark, "form": form}
            )


def delete_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    bookmark.delete()
    return redirect("bookmarks:index")


def move_bookmark_to_history(request, pk):
    bookmark = Bookmark.objects.get(id=pk)

    entry = Entry(
        user=bookmark.user,
        title=bookmark.title,
        year=bookmark.year,
        posterpath=bookmark.posterpath,
        tmdb_id=bookmark.tmdb_id,
        description=bookmark.description,
        media_type=bookmark.media_type,
        date_watched=date.today(),
    )
    entry.save()

    bookmark.delete()

    return redirect("history:index")
