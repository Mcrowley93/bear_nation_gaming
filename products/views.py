from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {"products": products})


# products_search function is case insensitive and gets the 'query' and filters the Products based on name
def products_search(request):
    products = Product.objects.filter(name__icontains=request.GET['query'])
    return render(request, "products/all_products.html", {"products": products})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_details.html', {'product': product})
