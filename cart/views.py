from django.shortcuts import render

from .cart import Cart


def cart_summary(request):

    cart = Cart(request)

    return render(request, 'cart/cart-summary.html', {'cart':cart})



