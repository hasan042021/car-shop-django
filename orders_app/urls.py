from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile_history, name="profile"),
    path("create/<int:id>/", views.create_order, name="create_order"),
]
