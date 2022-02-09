"""
Django settings for millm project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8$#zrmp#we6%i85q^b41+uyfua4=(&$nbgr1ud+fn2-_(kz7=o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.1.222', 'ht.xyz.local', 'cuzco.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'django.contrib.sites', #am#ph
   'photologue',           #am#ph
   'sortedm2m',            #am#ph
   'millm',
   'photologue_custom',
   'django_extensions',
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

ROOT_URLCONF = 'millm.urls'

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
            ],
        },
    },
]

#breakpoint()


WSGI_APPLICATION = 'millm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'my.cnf')
        },
    },
    
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        'NAME': os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        'USER': os.environ.get("SQL_USER", "user"),
        'PASSWORD': os.environ.get("SQL_PASSWORD", "password"),
        'HOST': os.environ.get("SQL_HOST", "localhost"),
        'PORT': os.environ.get("SQL_PORT", "5432"),
    },
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if not os.environ.get("DOCKER", False):
   DATABASES['default'] = DATABASES['mysql']
   print(DATABASES['default'])

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static') #am#ph
STATIC_URL = '/static/'                                  #am#ph
                                                         #am#ph
MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')   #am#ph
MEDIA_URL = '/media/'                                    #am#ph
                                                         #am#ph
STATICFILES_DIRS = (                                     #am#ph
    os.path.join(BASE_DIR, 'millm', 'static'),           #am#ph
)                                                        #am#ph
                                                         #am#ph
SITE_ID = 1                                              #am#ph

#print(photoprologue.PHOTOLOGUE_APP_DIR)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'drizla@inbox.ru'
EMAIL_HOST_PASSWORD = 'cK48DPqWv3VH76WFeB6p'
