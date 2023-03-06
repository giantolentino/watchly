from django.urls import path
from .views import BookmarksView


app_name = "accounts"
urlpatterns = [
    path("", BookmarksView.as_view(), name="homepage"),
]
