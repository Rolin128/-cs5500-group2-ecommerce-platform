"""
WSGI configuration for the ecommerce project.

This module exposes the WSGI callable as a variable named `application`.
It is used to deploy the Django application.

For detailed information on WSGI and its configuration, refer to:
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'ecommerce' Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# Create the WSGI application callable, which Django's servers and external servers will use
application = get_wsgi_application()
