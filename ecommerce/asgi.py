"""
ASGI configuration for the ecommerce project.

This module exposes the ASGI callable as a variable named `application`.
ASGI (Asynchronous Server Gateway Interface) allows handling asynchronous requests.

For more details on ASGI configuration, see:
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application


