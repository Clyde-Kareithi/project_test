from django import forms
from .models import CarCommerce
from .models import CarModel

class CarCommerceForm(forms.ModelForm):
    class Meta:
        models = CarCommerce
        fields = ['name', 'brand', 'description', 'price']

class YourCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['car_name', 'description', 'quantity', 'price', 'brand', 'car_images']

    def __init__(self, *args, **kwargs):
        super(YourCarForm, self).__init__(*args, **kwargs)
        self.fields['car_images'].widget.attrs['multiple'] = True
        self.fields['car_images'].widget.attrs['accept'] = 'image/*'