from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login.as_view(), name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/edit", views.edit_profile.as_view(), name="edit_profile"),
    path("passchange/", views.pass_change, name="pass_change"),
]
