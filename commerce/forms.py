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
        fields = ['car_name', 'description', 'quantity', 'price', 'brand', 'image']

    def __init__(self, *args, **kwargs):
        super(YourCarForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['multiple'] = True
        self.fields['image'].widget.attrs['accept'] = 'image/*'
        
        
        
class RecommendationForm(forms.Form):
    price = forms.IntegerField(
        label='Enter budget for the car:',
        required=True
    )
    
    body_style = forms.ChoiceField(
        label="What car body style are you looking for?", 
        choices=((1, 'Sedan'), (2, 'Hatchback'), (3, 'SUV/CUV'), (4, 'Wagon')),  
        widget=forms.RadioSelect, 
        initial='1',
        required=True
    )
    
    usecase = forms.ChoiceField(
        label="How will you use your car?", 
        choices=((1, 'Long Distance'), (2, 'Short Distance'), (3, 'Commercial'), (4, 'Sports Car')),  
        widget=forms.RadioSelect, 
        initial='2',
        required=True
    )
    
    brands = forms.ChoiceField(
        label="What brand would you be interested in?", 
        choices=((1, 'Audi'), (2, 'Short Distance'), (3, 'Commercial'), (4, 'Sports Car')),  
        widget=forms.RadioSelect, 
        initial='2',
        required=True
    )