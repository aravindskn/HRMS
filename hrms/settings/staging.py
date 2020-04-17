"""
This module contains configuration settings for staging environment.
"""

# pylint: disable=W0622
# pylint: disable=W0614
# pylint: disable=W0401
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'hrms-backend.innoventestech.in',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hrms',
        'TEST': {
            'NAME': 'test_hrms',
        },
        'USER': 'hrmsdbadmin',
        'PASSWORD': 'hrmsAdm3#n',
        'OPTIONS': {
            'autocommit': True,
        },
        'ATOMIC_REQUESTS': True
    }
}

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
    'hrms.innoventestech.in'
)

CSRF_TRUSTED_ORIGINS = (
    'localhost:3000',
    'hrms.innoventestech.in'
)
