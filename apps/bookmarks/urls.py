from django.urls import path
from .views import BookmarksView


app_name = "bookmarks"
urlpatterns = [
    path("", BookmarksView.as_view(), name="bookmarks"),
]
