from .base import *

import authkey

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = authkey.EMAIL_HOST
EMAIL_HOST_USER = authkey.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = authkey.EMAIL_HOST_PASSWORD
EMAIL_PORT = authkey.EMAIL_PORT
EMAIL_USE_TLS = authkey.EMAIL_USE_TLS
DEFAULT_FROM_EMAIL = authkey.DEFAULT_FROM_EMAIL
SERVER_EMAIL = authkey.DEFAULT_FROM_EMAIL
DATABASES_NAME = authkey.DATABASES_NAME
DATABASES_USER = authkey.DATABASES_USER
DATABASES_PASSWORD = authkey.DATABASES_PASSWORD
DATABASES_HOST = authkey.DATABASES_HOST

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASES_NAME,
        'USER': DATABASES_USER,
        'PASSWORD': DATABASES_PASSWORD,
        'HOST': DATABASES_HOST,
        'PORT': '3306',
        'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                }
    }
}

INSTALLED_APPS = INSTALLED_APPS +[
    'storages',
]

DATABASES['default']['ATOMIC_REQUESTS'] = True

INTERNAL_IPS = ('127.0.0.1', 'localhost',)

AWS_STORAGE_BUCKET_NAME = authkey.BUCKET_NAME
AWS_ACCESS_KEY_ID = authkey.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = authkey.AWS_SECRET_ACCESS_KEY
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_HOST = authkey.AWS_S3_HOST
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'djangostarter.storage.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'djangostarter.storage.MediaStorage'