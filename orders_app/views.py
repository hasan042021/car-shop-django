from django.shortcuts import render, redirect
from cars_app.models import Car
from . import models


# Create your views here.
def profile_history(request):
    my_orders = models.Order.objects.filter(user=request.user.id)
    return render(
        request, "profile_history.html", {"user": request.user, "orders": my_orders}
    )


def create_order(request, id):
    purchased_car = Car.objects.get(pk=id)
    purchased_car.quantity -= 1
    purchased_car.save()
    newOrder = models.Order()
    newOrder.car = purchased_car
    newOrder.user = request.user
    newOrder.save()
    return redirect("car_details", id=id)
