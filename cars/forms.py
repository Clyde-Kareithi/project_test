from django import forms
from .models import CarModel


class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        # fields = ['name', 'bio']

class YourCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['car_name', 'price', 'brand', 'image']