from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("register/", views.Register.as_view(), name="register"),
    path("profile/", views.Profile.as_view(), name="profile")
]
