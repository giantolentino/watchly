from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Entry
from django.shortcuts import get_object_or_404, redirect


class HistoryView(ListView):
    model = Entry
    context_object_name = "entries"
    template_name = "history/index.html"

    def get_queryset(self):
        queryset = Entry.objects.filter(user=self.request.user).order_by("-date_added")
        return queryset


class HistoryDetailView(DetailView):
    model = Entry
    template_name = "history/detailed.html"
    context_object_name = "entry"


def delete_history(request, pk):
    history = get_object_or_404(Entry, pk=pk)
    history.delete()
    return redirect("history:index")
