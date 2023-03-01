from django.urls import path
from .views import HomePageView, LoginView


app_name = "accounts"
urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("login/", LoginView.as_view(), name="login"),
]
