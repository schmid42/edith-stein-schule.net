import os

from .base import *

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = "http://localhost:8000"

WAGTAILADMIN_BASE_URL = "http://localhost:8000/admin"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': os.getenv('DATABASE_NAME'),
#        'USER': os.getenv('DATABASE_USER'),
#        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
#        'HOST': os.getenv('DATABASE_HOST'),
#        'PORT': os.getenv('DATABASE_PORT'),
#    }
#}

try:
    from .local import *
except ImportError:
    pass
