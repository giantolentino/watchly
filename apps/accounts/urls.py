from django.urls import path
from .views import HomePageView, LoginView, LogoutView, RegisterView, TestPageView


app_name = "accounts"
urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("test/", TestPageView.as_view(), name="test"),
]
