from django.urls import path
from products.views import all_products, products_search, product_details, add_review_to_product

urlpatterns = [
    path('all_products/', all_products, name='all_products'),
    path('product_details/<int:pk>/', product_details, name='product_details'),
    path('products_search', products_search, name='products_search'),
    path('product/<int:pk>/review/', add_review_to_product, name='add_review_to_product'),

]
