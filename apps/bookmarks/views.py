from django.views.generic import TemplateView


# Create your views here.
class BookmarksView(TemplateView):
    template_name = "bookmarks/bookmarks.html"
