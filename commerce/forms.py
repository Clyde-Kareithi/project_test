from django import forms
from .models import CarCommerce

class CarCommerceForm(forms.ModelForm):
    class Meta:
        models = CarCommerce
        fields = ['name', 'brand', 'description', 'price']