from pathlib import Path

# Define the base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-olc_l4v9uimldmd)xjf0qcgbl#f3zyln(b##@b26_&2q_oo@_d'

# SECURITY WARNING: Don’t run with debug turned on in production!
DEBUG = True

# Define allowed hosts
ALLOWED_HOSTS = ['*']  # Adjust for production, e.g., ['mywebsite.com']

# Uncomment to set CSRF trusted origins, if needed
# CSRF_TRUSTED_ORIGINS = ['https://www.edenthought.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',  # Custom app for store
    'cart',   # Custom app for cart
    'account', # Custom app for account
    'payment', # Custom app for payment
    'mathfilters',
    'crispy_forms', # Crispy forms for better styling
    'storages', # AWS S3 storage support
]

# Cross-Origin Opener Policy
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

# Crispy Forms Template Pack
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.views.categories',  # Additional context for categories
                'cart.context_processors.cart',  # Custom context for cart
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database configuration (using SQLite for local development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and media files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'static/media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration for sending password reset emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''  # Enter your GMAIL address
EMAIL_HOST_PASSWORD = ''  # Enter your app password

# Uncomment and set AWS credentials for S3 storage if needed
'''
AWS_ACCESS_KEY_ID = "" # Access Key ID
AWS_SECRET_ACCESS_KEY = "" # Secret Access Key
AWS_STORAGE_BUCKET_NAME = '' 
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False
'''

# Uncomment and configure for PostgreSQL or RDS database settings, if needed
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',  # Database name
        'USER': '',  # Database user
        'PASSWORD': '',  # Database password
        'HOST': '',  # Database host
        'PORT': '5432',  # Database port
    }
}
'''