from django.views.generic import ListView
from django.conf import settings
from django.views import View
from django.shortcuts import render
from datetime import datetime
from requests import get
import requests
from apps.bookmarks.forms import BookmarkForm
from apps.history.forms import HistoryEntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib import messages


API_KEY = settings.TMDB_API_KEY
base_url = "https://api.themoviedb.org/3/"


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


class DetailedView(View):
    def get(self, request, result_id):
        type = request.GET.get("type")
        youtube_url = get_youtube_url(result_id, type)
        result, title, year, date = get_result_data(result_id, type)

        bookmark_form = BookmarkForm(
            request.POST or None,
            initial={
                "title": title,
                "year": year,
                "posterpath": result["poster_path"],
                "description": result["overview"],
                "media_type": type,
                "tmdb_id": result_id,
            },
        )

        history_form = HistoryEntryForm(
            request.POST or None,
            initial={
                "title": title,
                "year": year,
                "posterpath": result["poster_path"],
                "description": result["overview"],
                "media_type": type,
                "tmdb_id": result_id,
            },
        )

        return render(
            request,
            "search/detailed.html",
            {
                "result": result,
                "title": title,
                "year": year,
                "date": date,
                "trailer": youtube_url,
                "bookmark_form": bookmark_form,
                "history_form": history_form,
            },
        )

    def post(self, request, result_id):
        type = request.GET.get("type")
        youtube_url = get_youtube_url(result_id, type)
        result, title, year, date = get_result_data(result_id, type)

        bookmark_form = BookmarkForm(request.POST or None)
        history_form = HistoryEntryForm(request.POST or None)

        if bookmark_form.is_valid() or history_form.is_valid():
            bookmark_form.instance.user = request.user
            history_form.instance.user = request.user

            try:
                bookmark_form.save()
                history_form.save()
                return HttpResponseRedirect(reverse_lazy("bookmarks:index"))
            except IntegrityError:
                bookmark_form.add_error(None, "Bookmark already exists.")
        else:
            messages.error(request, "Please correct the errors below.")

        return render(
            request,
            "search/detailed.html",
            {
                "result": result,
                "title": title,
                "year": year,
                "date": date,
                "trailer": youtube_url,
                "bookmark_form": bookmark_form,
                "history_form": history_form,
            },
        )


def get_result_data(result_id, type):
    if type == "tv":
        url = f"{base_url}tv/{result_id}?api_key={API_KEY}"
        response = get(url)
        result = response.json()

        title = result["name"]
        year = result["first_air_date"][:4]
        date = change_date_format(result["first_air_date"])

    else:
        url = f"{base_url}movie/{result_id}?api_key={API_KEY}"
        response = get(url)
        result = response.json()

        title = result["title"]
        year = result["release_date"][:4]
        date = change_date_format(result["release_date"])
    return result, title, year, date


def get_youtube_url(result_id, type):
    if type == "tv":
        url = f"{base_url}tv/{result_id}/videos?api_key={API_KEY}"
    else:
        url = f"{base_url}movie/{result_id}/videos?api_key={API_KEY}"

    trailer_response = get(url)
    videos = trailer_response.json()["results"]

    # find the trailer in the videos array
    trailer = next((video for video in videos if video["type"] == "Trailer"), None)

    if trailer:
        return f"https://www.youtube.com/embed/{trailer['key']}"
    else:
        return None


def change_date_format(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    return date.strftime("%m-%d-%Y")
