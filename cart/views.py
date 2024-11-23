from django.shortcuts import render
from .cart import Cart
from store.models import Product, Category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def cart_summary(request):
    cart = Cart(request)
    categories = Category.objects.all()
    
    # Validate product images exist
    for item in cart:
        product = item['product']
        if not product.image or not hasattr(product.image, 'url'):
            # Set a flag to indicate missing image
            item['image_missing'] = True
    
    return render(request, 'cart/cart-summary.html', {
        'cart': cart,
        'categories': categories,
    })

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        
        # Check if adding this quantity would exceed 99
        current_qty = 0
        if str(product_id) in cart.cart:
            current_qty = cart.cart[str(product_id)]['qty']
        
        # Calculate total quantity after addition
        total_qty = current_qty + product_quantity
        
        # Add to cart
        cart.add(product=product, product_qty=product_quantity)
        cart_quantity = cart.__len__()
        
        # Return exceeded flag if total would exceed 99
        response = JsonResponse({
            'qty': cart_quantity,
            'exceeded': total_qty > 99
        })
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total()
        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})
        return response



def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        
        # Validate quantity doesn't exceed 99
        if product_quantity > 99:
            product_quantity = 99
        elif product_quantity < 1:
            product_quantity = 1
            
        cart.update(product=product_id, qty=product_quantity)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total()
        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})
        return response
