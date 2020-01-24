from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {"products": products})


# products_search function is case insensitive and gets the 'query' and filters the Products based on name
def products_search(request):
    products = Product.objects.filter(name__icontains=request.GET['query'])
    return render(request, "products/all_products.html", {"products": products})
