from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

from . models import ShippingAddress, Order, OrderItem

from cart.cart import Cart

from django.http import JsonResponse


def checkout(request):

    # Get cart
    cart = Cart(request)
    
    # Check if cart is empty or total is 0
    if not cart.get_total():
        messages.error(request, "Your cart is empty. Please add items before checking out.")
        return redirect('cart-summary')

    # Users with accounts -- Pre-fill the form

    if request.user.is_authenticated:

        try:

            # Authenticated users WITH shipping information 

            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = {'shipping': shipping_address}

            


            return render(request, 'payment/checkout.html', context=context)


        except:

            # Authenticated users with NO shipping information

            return render(request, 'payment/checkout.html')

    else:
            
        # Guest users

        return render(request, 'payment/checkout.html')



def complete_order(request):

    if request.POST.get('action') == 'post':

        name = request.POST.get('name')
        email = request.POST.get('email')

        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')

        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')


        # All-in-one shipping address

        shipping_address = (address1 + "\n" + address2 + "\n" +
        
        city + "\n" + state + "\n" + zipcode
        
        )

        # Shopping cart information 

        cart = Cart(request)


        # Get the total price of items

        total_cost = cart.get_total()


        '''

            Order variations

            1) Create order -> Account users WITH + WITHOUT shipping information
        

            2) Create order -> Guest users without an account
        

        '''

        # 1) Create order -> Account users WITH + WITHOUT shipping information

        if request.user.is_authenticated:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address,
            
            amount_paid=total_cost, user=request.user)


            order_id = order.pk

            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                
                price=item['price'], user=request.user)


        #  2) Create order -> Guest users without an account

        else:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address,
            
            amount_paid=total_cost)


            order_id = order.pk


            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                
                price=item['price'])




        order_success = True

        response = JsonResponse({'success':order_success})

        return response




    

    




def mock_payment(request):
    """
    Display the mock payment form for testing purposes.
    """
    # Get cart
    cart = Cart(request)
    
    # Check if cart is empty or total is 0
    if not cart.get_total():
        messages.error(request, "Your cart is empty. Please add items before checking out.")
        return redirect('cart-summary')
        
    return render(request, 'payment/mock_payment.html')

def mock_payment_process(request):
    """
    Process the mock payment and create the order.
    """
    if request.method != 'POST':
        return redirect('checkout')

    # Get cart
    cart = Cart(request)
    
    if not cart.get_total():
        messages.error(request, "Your cart is empty. Please add items before checking out.")
        return redirect('cart-summary')

    # Create order
    if request.user.is_authenticated:
        order = Order.objects.create(
            full_name=request.user.get_full_name(),
            email=request.user.email,
            shipping_address="Test Address",  # You might want to get this from the session
            amount_paid=cart.get_total(),
            user=request.user,
            status="Placed"  # Set the order status to "Placed"
        )

        for item in cart:
            OrderItem.objects.create(
                order_id=order.pk,
                product=item['product'],
                quantity=item['qty'],
                price=item['price'],
                user=request.user
            )
    else:
        order = Order.objects.create(
            full_name="Test User",  # You might want to get this from the session
            email="test@example.com",  # You might want to get this from the session
            shipping_address="Test Address",  # You might want to get this from the session
            amount_paid=cart.get_total(),
            status="Placed"  # Set the order status to "Placed"
        )

        for item in cart:
            OrderItem.objects.create(
                order_id=order.pk,
                product=item['product'],
                quantity=item['qty'],
                price=item['price']
            )

    # Clear the cart by removing the session key
    if 'session_key' in request.session:
        del request.session['session_key']
        request.session.modified = True

    # Redirect to success page
    return redirect('payment-success')


def payment_success(request):
    # Clear shopping cart
    for key in list(request.session.keys()):
        if key == 'session_key':
            del request.session[key]
    return render(request, 'payment/payment-success.html')


def payment_failed(request):
    return render(request, 'payment/payment-failed.html')
