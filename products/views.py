from django.shortcuts import render
from .models import Product
from django.contrib.admin.views.decorators import staff_member_required


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {"products": products})

# @staff_member_required