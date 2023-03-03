from django.views.generic import ListView
from django.conf import settings
import requests


API_KEY = settings.TMDB_API_KEY


class SearchResultsView(ListView):
    template_name = "search/results.html"
    context_object_name = "results"
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get("q")
        url = (
            f"https://api.themoviedb.org/3/search/multi?api_key={API_KEY}&query={query}"
        )
        response = requests.get(url)
        results = response.json()["results"]
        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        return context
