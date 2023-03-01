from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


class HomePageView(TemplateView):
    template_name = "accounts/homepage.html"


class LoginView(LoginView):
    template_name = "accounts/login.html"
