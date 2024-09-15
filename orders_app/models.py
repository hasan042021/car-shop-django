from django.db import models
from cars_app.models import Car
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f" user: {self.user.first_name} - car: {self.car.car_name}"
