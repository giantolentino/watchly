from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView


class HomePageView(TemplateView):
    template_name = "accounts/homepage.html"


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
