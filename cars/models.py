from django.db import models

# Create your models here.


class BrandModel(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=500, unique=True, null=True)

    def __str__(self) -> str:
        return self.brand_name


USECASE_CHOICES = (
    ("LONG_DISTANCE", "Long Distance"),
    ("COMMERCIAL", "Commercial"),
    ("SPORTS_CAR", "Sports Cars"),
    ("SHORT_DISTANCE", "Short Distance"),
    ("COLLECTORS_ITEM", "Collectors Item")
)

FUEL_TYPE_CHOICES = (
   ("PETROL", "Petrol"),
   ("DIESEL", "Diesel"), 
   ("HYBRID", "Hybrid" ),
   ("ELETRIC", "Electric" ),
)

class CarModel(models.Model):
    car_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    usecase = models.CharField(max_length=20, choices=USECASE_CHOICES, default="SHORT_DISTANCE")
    fuel_type = models.CharField(max_length=7, choices=FUEL_TYPE_CHOICES, default='PETROL')
    year = models.PositiveSmallIntegerField(default=2017) # Ano de fabricação
    image = models.ImageField(upload_to='cars/media/uploads/')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.car_name
