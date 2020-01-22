from django.urls import path
from products.views import all_products, products_search
# , product_details

urlpatterns = [
    path('products/', all_products, name='all_products'),
    # path('product_details/', product_details, name='product_details'),
    path('products_search', products_search, name='products_search'),
]
