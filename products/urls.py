from django.urls import path
from . import views
from products.views import all_products
# , product_details

urlpatterns = [
    path('products/', all_products, name='all_products'),
    # path('product_details/', product_details, name='product_details'),
]
