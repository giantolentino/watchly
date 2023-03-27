from django.urls import path
from .views import (
    BookmarksView,
    BookmarkDetailView,
    delete_bookmark,
    move_bookmark_to_history,
)


app_name = "bookmarks"
urlpatterns = [
    path("", BookmarksView.as_view(), name="index"),
    path("<int:pk>/", BookmarkDetailView.as_view(), name="detailed"),
    path("delete/<int:pk>", delete_bookmark, name="delete"),
    path("move/<int:pk>", move_bookmark_to_history, name="move"),
]
