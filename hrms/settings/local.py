"""
This module contains configuration settings for local environment.
"""

# pylint: disable=W0622
# pylint: disable=W0614
# pylint: disable=W0401
from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)

CSRF_TRUSTED_ORIGINS = (
    'localhost:3000',
)
