from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Entry
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UpdateHistoryForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UpdateHistoryForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        history_entry = self.get_object()
        form = UpdateHistoryForm(request.POST, instance=history_entry)
        if form.is_valid():
            form.save()
            return render(
                request, self.template_name, {"entry": history_entry, "form": form}
            )
        else:
            return render(
                request, self.template_name, {"entry": history_entry, "form": form}
            )


def delete_history(request, pk):
    history = get_object_or_404(Entry, pk=pk)
    history.delete()
    return redirect("history:index")


def sort_by(queryset, filter_by):
    ordering = {
        "1": "title",
        "2": "-title",
        "3": "date_added",
        "4": "-date_added",
        "5": "date_watched",
        "6": "-date_watched",
        "7": "-rating",
        "8": "rating",
    }
    return queryset.order_by(ordering.get(filter_by, "-date_added"))
