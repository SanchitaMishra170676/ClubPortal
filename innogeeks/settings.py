"""
Django settings for innogeeks project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from .config import AMAZON_CREDENTIAL


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '####'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']



SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True 


# Application definition

INSTALLED_APPS = [
    
    'accounts',
    'home',
    'dashboard',
    'member',
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'innogeeks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'innogeeks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }


DATABASES = {
     'default':{
	'ENGINE': 'django.db.backends.mysql',
	'OPTIONS': {
	    'read_default_file': '/etc/mysql/my.cnf',
	},
     }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'innogeeksdb',
#         'USER': 'postgres',
#         'PASSWORD': 'Shnd@9897',
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'innogeeksdb',
#         'USER': 'innogeeks',
#         'PASSWORD': 'innogeeks2021',
#         'HOST': 'ec2-13-126-93-35.ap-south-1.compute.amazonaws.com',
#         'PORT': 5433
#     }
# }


# EMAIL_BACKEND=  'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST= 'smtp.gmail.com'
# EMAIL_PORT= 587
# # EMAIL_HOST_USER= os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_USER= 'innogeeks@kiet.edu'
# # # EMAIL_HOST_PASSWORD= os.environ.get('EMAIL_HOST_PASSWORD')
# # EMAIL_HOST_PASSWORD = 'ucmdayzsxpdvubjb'
# EMAIL_HOST_PASSWORD = 'dnunusmlcrkbdvsi'
# # dnunusmlcrkbdvsi

# EMAIL_USE_TLS= True

EMAIL_BACKEND=  'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 587
# EMAIL_HOST_USER= os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_USER= 'innogeeks@kiet.edu'
# # EMAIL_HOST_PASSWORD= os.environ.get('EMAIL_HOST_PASSWORD')
# EMAIL_HOST_PASSWORD = 'ucmdayzsxpdvubjb'
EMAIL_HOST_PASSWORD = 'qupzsgbrxdmkqkje'
# dnunusmlcrkbdvsi

EMAIL_USE_TLS= True




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
    # ...
    "dashboard.views.clubprofile",
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'



AWS_ACCESS_KEY_ID = AMAZON_CREDENTIAL['ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = AMAZON_CREDENTIAL['SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = AMAZON_CREDENTIAL['STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = False
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}
# static_location ='static'
PUBLIC_STATIC_LOCATION = 'static'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_STATIC_LOCATION}/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'



MEDIAFILES_LOCATION = 'media'

