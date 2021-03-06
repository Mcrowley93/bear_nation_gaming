from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Productreview
from .forms import ProductReviewForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages


def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    return render(request, 'products/all_products.html', {"products": paged_products})


# products_search function is case insensitive and gets the 'query' and filters the Products based on name
def products_search(request):
    products = Product.objects.filter(name__icontains=request.GET['query']) | Product.objects.filter(price__icontains=request.GET['query'])
    return render(request, "products/all_products.html", {"products": products})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_details.html', {'product': product})


@login_required()
def add_review_to_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product_review_form = ProductReviewForm(request.POST)
        if product_review_form.is_valid():
            product_review = product_review_form.save(commit=False)
            product_review.reviewer = request.user
            product_review.product = product
            product_review.save()
            return redirect('product_details', pk=product.pk)
    else:
        product_review_form = ProductReviewForm()
    return render(request, 'products/add_review_to_product.html', {'product_review_form': product_review_form})


@login_required()
def delete_product_review(request, pk):
    product_review = get_object_or_404(Productreview, pk=pk)
    if request.user != product_review.reviewer:
        messages.error(request, "You can only delete product reviews you have previously submitted!")
        return redirect('all_products')
    product_review.delete()
    return redirect('all_products')
