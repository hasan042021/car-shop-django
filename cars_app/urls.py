from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.car_details.as_view(), name="car_details"),
]
