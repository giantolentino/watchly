from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.shortcuts import get_object_or_404, redirect
from .forms import UpdateBookmarkForm
from django.shortcuts import render


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
