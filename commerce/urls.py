from django.urls import path
from . import views


urlpatterns = [
    path("sell", views.sell_car, name="sell_car"),
    path("recommendations", views.get_recommended_cards, name="recommender"),
]

