from django.shortcuts import render

from . models import Category, Product

from django.shortcuts import get_object_or_404


def store(request):
    # Get all products and categories
    products = Product.objects.all()
    categories = Category.objects.all()

    # Initialize context with basic data
    context = {
        'products': products,
        'categories': categories
    }

    # Add personalized content for logged-in users
    if request.user.is_authenticated:
        # Get recently viewed products from session
        recent_product_ids = request.session.get('recent_products', [])
        recent_items = Product.objects.filter(id__in=recent_product_ids)[:4]
        
        # Get recommended products (simple implementation - can be enhanced)
        # For now, just get products from categories the user has viewed
        user_categories = set()
        for product in recent_items:
            user_categories.add(product.category.id)
        
        recommended_items = Product.objects.filter(
            category__id__in=user_categories
        ).exclude(
            id__in=recent_product_ids
        ).order_by('?')[:4]  # Random selection for now

        context.update({
            'recent_items': recent_items,
            'recommended_items': recommended_items
        })

    return render(request, 'store/store.html', context)



def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}



def list_category(request, category_slug=None):

    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)


    return render(request, 'store/list-category.html', {'category':category, 'products':products})



def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    # Track recently viewed products for logged-in users
    if request.user.is_authenticated:
        # Get existing list from session
        recent_products = request.session.get('recent_products', [])
        
        # Remove the product if it's already in the list
        if product.id in recent_products:
            recent_products.remove(product.id)
            
        # Add the product to the beginning of the list
        recent_products.insert(0, product.id)
        
        # Keep only the last 10 viewed products
        recent_products = recent_products[:10]
        
        # Update session
        request.session['recent_products'] = recent_products
        request.session.modified = True

    context = {'product': product}
    return render(request, 'store/product-info.html', context)
