from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CarCommerce
from cars.models import CarModel, BrandModel

# Create your views here.
@login_required
def sell_car(request, car_name, description, brand, quantity,  price, image):
    existing_brand = BrandModel.objects.get_or_create(brand_name=brand)
    car = CarModel.objects.create(car_name=car_name, description=description, brand=existing_brand, quantity=quantity, price=price, image=image)
    current_user = request.user
    car_for_sale = CarCommerce.objects.create(car=car, user=current_user)
    car_for_sale.save()

    return car_for_sale




            

