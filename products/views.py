from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {"products": products})


def products_search(request):
    products = Product.objects.filter(name__icontains=request.GET['query'])
    return render(request, "products/all_products.html", {"products": products})
