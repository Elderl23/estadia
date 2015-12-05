"""
Django settings for topicos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Path(__file__).ancestor(2)
PROYECT_ROOT = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h-e$5t8zzrj+&i3v^j3u&3=c*)n*w&h^c@a_c^8ij*(4-t*$uh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.estadia',
)

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('u-app:inicio')
LOGIN_REDIRECT_URL = reverse_lazy('u-app:inicio')
LOGOUT_URL = reverse_lazy('u-app:salir')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'topicos.urls'

WSGI_APPLICATION = 'topicos.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROYECT_ROOT, 'template'),
    PROYECT_ROOT + 'template',
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME'    : 'd5ug66cu689l1g',
        'USER'    : 'fzwjmweaebgzqv',
        'PASSWORD':'E_r2sChKMcTpG5NEhmwVOndmZC',
        'HOST':'ec2-107-21-219-142.compute-1.amazonaws.com',
        'PORT':'5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_URL = '/media/'

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_DIRS = [
#BASE_DIR.child('topicos').child('static')
os.path.join(PROYECT_ROOT, 'static'),
]



