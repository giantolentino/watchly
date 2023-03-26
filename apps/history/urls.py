from django.urls import path
from .views import HistoryView, HistoryDetailView

app_name = "history"
urlpatterns = [
    path("", HistoryView.as_view(), name="index"),
    path("<int:pk>/", HistoryDetailView.as_view(), name="detailed"),
]
