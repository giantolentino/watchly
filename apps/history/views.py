from django.views.generic import TemplateView


class HistoryView(TemplateView):
    template_name = "history/index.html"
