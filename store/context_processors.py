from .models import Category

def categories(request):
    """
    Context processor to make categories available across all templates
    """
    return {
        'categories': Category.objects.all()
    }
