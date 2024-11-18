# Import necessary Django modules and functions
from django.conf import settings  # Access project settings like MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static  # Serve static and media files during development
from django.contrib import admin  # Django admin site
from django.urls import path, include  # Functions to define URL patterns

# Define the URL patterns for the project
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Store application URLs
    path('', include('store.urls')),

    # Cart application URLs
    path('cart/', include('cart.urls')),

    # Account application URLs
    path('account/', include('account.urls')),

    # Payment application URLs
    path('payment/', include('payment.urls')),

    # Chatbot application URLs
    path('chatbot/', include('chatbot.urls')), 
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
