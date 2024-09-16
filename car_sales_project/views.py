from django.shortcuts import render
from cars_app.models import Car, Brand


def home(request, brand_slug=None):

    data = Car.objects.all()
    filter = None
    if brand_slug is not None:
        brand = Brand.objects.get(slug=brand_slug)
        data = Car.objects.filter(brand=brand)
        filter = brand.brand_name

    brands = Brand.objects.all()
    return render(
        request, "home.html", {"data": data, "brands": brands, "filter": filter}
    )
