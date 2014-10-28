# -*- coding: utf-8 -*-

"""
Django settings for abftecnologia project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

from django.core.urlresolvers       import reverse

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iifg81iorlk=0e$mo8r3l0i8us*np)*#vcf=22yp%$ib-j)z$5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

LOCAL = False # Marca se o projeto esta em desenvolvimento


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',            

    # aplicações de terceiros
    'easy_thumbnails',
    'image_cropping',
    'social_auth',

    # aplicações da abftecnologia
    'utils',
    'multimidia',
    
    # aplicações do projeto    
    'biblioteca',	
    'portifolio',
    'contato',
    'blog',
    'home',
    'rodape',
    'cliente',        
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",

    "social_auth.context_processors.social_auth_by_type_backends",
        
    "rodape.context_processors.conteudo_rodape",
)



SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


ROOT_URLCONF = 'abftecnologia.urls'

WSGI_APPLICATION = 'abftecnologia.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'abftecnologia',
        'USER': 'abftecnologia',
        'PASSWORD': 'abftecnologia',
        'HOST': 'mysql.abftecnologia.com.br',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

STATICFILES_DIRS = (
    ('site',os.path.join(PROJECT_PATH, 'sitestatic')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# Arquivos enviados pelo usuario via upload

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MEDIA_URL = '/media/'

# Localização dos templates do projeto
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)


# Configuração de envio de email
EMAIL_BACKEND           = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST              = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER         = 'AKIAIK3DDGSKLMZGE2DA'
EMAIL_HOTS_PASSWORD     = 'AgKxlnjeZVyia6Yq8+XreQs9L7LHaGxiJvg2xbC5Kw0z'
EMAIL_PORT              = 465
EMAIL_USE_TLS           = True

SITE_URL        = 'http://abftecnologia.com.br'
EMAIL_REMETENTE = 'contato@abftecnologia.com.br'

# Configuração do Grappelli
GRAPPELLI_ADMIN_TITLE = "ABF Tecnologia"
GRAPPELLI_INDEX_DASHBOARD = 'abftecnologia.somefile.CustomIndexDashboard'

# Configuração de perfil personalizado do usuario
AUTH_PROFILE_MODULE = 'cliente.UserProfile'

#Adiciona o backend do Facebook e mantém o do Django vivo
AUTHENTICATION_BACKENDS = (    
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#Configurações de login do próprio Django
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/minha-area/'

#Social Auth
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = reverse('cliente_sucesso')

#Facebook
FACEBOOK_APP_ID = '295956483900055'
FACEBOOK_API_SECRET = '98a44999b93447a9cf7bc3721deb9444'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}

# Configuração do easy_thumbnails, image_cropping 
from easy_thumbnails.conf import settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS
