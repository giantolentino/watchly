from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class HomePageView(TemplateView):
    template_name = "accounts/homepage.html"


class LoginView(LoginView):
    template_name = "accounts/login.html"


class LogoutView(LogoutView):
    next_page = reverse_lazy("accounts:homepage")
