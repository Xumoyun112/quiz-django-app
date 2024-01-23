from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quizdb',
        'USER': 'postgres',
        'PASSWORD': '102938',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# STATICFILES_DIRS = [BASE_DIR / '../static/']
