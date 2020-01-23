from django.urls import path
from cart.views import view_cart, add_to_cart, adjust_cart


urlpatterns = [
    path('view_cart/', view_cart, name="view_cart"),
    path('add_to_cart/<id>/', add_to_cart, name="add_to_cart"),
    path('adjust_cart/<id>/', adjust_cart, name="adjust_cart")
]
