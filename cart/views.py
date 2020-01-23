from django.shortcuts import render, reverse, redirect

"""
Code for cart views reused from the CI e-commerce mini-project, and re-purposed to fit the project's requirements
"""


def view_cart(request):
    """
    A View that renders the cart contents page
    """
    return render(request, "cart/cart.html")


def add_to_cart(request, id):
    """
    Add a quantity of a specified product to the cart
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('all_products'))


def adjust_cart(request, id):
    """
    Adjust the quantity of a specified product by a specified amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
