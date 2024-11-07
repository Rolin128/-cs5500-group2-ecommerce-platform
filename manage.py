#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""

import os
import sys

def main():
    """Run administrative tasks for the Django project."""
    
    # Set the default settings module for the Django project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    
    try:
        # Import the Django management command execution function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an error with a helpful message if Django isn't installed or configured correctly
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "properly configured in your PYTHONPATH environment variable. "
            "Also, verify that your virtual environment is activated, if applicable."
        ) from exc
    
    # Execute the Django management command
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()