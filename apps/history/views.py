from django.views.generic import ListView
from .models import Entry


class HistoryView(ListView):
    model = Entry
    context_object_name = "entries"
    template_name = "history/index.html"

    def get_queryset(self):
        queryset = Entry.objects.filter(user=self.request.user).order_by("-date_added")
        return queryset
