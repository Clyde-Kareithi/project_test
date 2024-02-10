from django.urls import path
from . import views


urlpatterns = [
    path("sell", views.sell_car, name="sell_car"),
    path("buy", views.buy_car, name="buy_car"),
]

