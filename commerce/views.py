from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CarCommerce
from cars.models import CarModel, BrandModel
from .forms import RecommendationForm, YourCarForm


def buy_car(request):
    # Get distinct body styles and brands
    body_styles = CarModel.objects.values_list('body_style', flat=True).distinct()
    brands = BrandModel.objects.all()

    if request.method == 'POST':
        # Handle form submission
        price = request.POST.get('price')
        body_style = request.POST.get('body_style')
        brand_id = request.POST.get('brand')

        # Perform further processing with the user inputs
        # For example, you can filter cars based on the user's choices
        selected_brand = BrandModel.objects.get(pk=brand_id)
        cars = CarModel.objects.filter(price__lte=price, body_style=body_style, brand=selected_brand)

        # You can then pass the filtered cars to the template or perform any other logic

    return render(request, 'buyer.html', {'body_styles': body_styles, 'brands': brands})


def sell_car(request): 
    seller_form = YourCarForm()
    if seller_form.is_valid():
        car = seller_form.save()
        commerce = CarCommerce.objects.create(car=car, user=request.user)
        commerce.save()
    return render(request, 'seller.html', {'seller_form': seller_form})


def get_recommended_cards(request):
    recommender_form = RecommendationForm()
    return render(request, "buyer.html", {'recommender_form': recommender_form})

def add_car(request):
    if request.method == 'POST':
        form = YourCarForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form or perform other actions
            form.save()
            return render(request, 'success_page.html')  # Redirect to a success page after saving

    else:
        form = YourCarForm()

    return render(request, 'sell.html', {'form': form})



            

