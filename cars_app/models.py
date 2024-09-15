from django.db import models


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    image = models.ImageField(upload_to="cars_app/media/uploads/")
    car_name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"
