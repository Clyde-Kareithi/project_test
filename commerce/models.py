from django.db import models
from django.contrib.auth.models import User
from cars.models import CarModel

# Create your models here.
class CarCommerce(models.Model):
    id = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' ' + self.car.car_name
