# Import necessary Django modules and functions
from django.conf import settings  # Access project settings like MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static  # Serve static and media files during development
from django.contrib import admin  # Django admin site
from django.urls import path, include  # Functions to define URL patterns



# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
