from django.urls import path

# from . import views
from .views import SearchResultsView, DetailedView

app_name = "search"

urlpatterns = [
    path("", SearchResultsView.as_view(), name="search"),
    path("tmdb/display/<int:result_id>", DetailedView.as_view(), name="detailed"),
]
