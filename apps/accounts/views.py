from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from apps.bookmarks.models import Bookmark
from apps.history.models import Entry


class HomePageView(TemplateView):
    template_name = "accounts/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookmarks"] = Bookmark.objects.filter(
            user_id=self.request.user.id
        ).order_by("-date_added")[:3]
        context["bookmark_count"] = Bookmark.objects.filter(
            user_id=self.request.user.id
        ).count()
        context["entries"] = Entry.objects.filter(
            user_id=self.request.user.id
        ).order_by("-date_added")[:3]
        context["history_count"] = Entry.objects.filter(
            user_id=self.request.user.id
        ).count()
        return context


class LoginView(LoginView):
    template_name = "accounts/login.html"


class LogoutView(LogoutView):
    next_page = reverse_lazy("accounts:homepage")


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"


class TestPageView(TemplateView):
    template_name = "accounts/test.html"
