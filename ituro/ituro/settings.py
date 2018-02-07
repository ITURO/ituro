"""
Django settings for ituro project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.utils.translation import ugettext_lazy as _
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '303y*!pxg_ioragt=zzy4&-@kq^mxb-e=mlgu2m426%4ud35l='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # 3rd party apps
    'bootstrap3',
    'captcha',

    # ITURO apps
    'accounts',
    'base',
    'lcd',
    'orders',
    'projects',
    'referee',
    'results',
    'sumo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'ituro.urls'

WSGI_APPLICATION = 'ituro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'tr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('tr', _('Turkish')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(
    os.path.join(BASE_DIR, os.pardir, "public", "static"))
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(
    os.path.join(BASE_DIR, os.pardir, "public", "media"))

TEMPLATE_CONTEXT_PROCESSORS =(
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "base.context_processors.permissions",
    "base.context_processors.categories",
)

AUTH_USER_MODEL = "accounts.CustomUser"
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
EMAIL_USE_TLS = True
MAX_FILE_SIZE = 1000000
LOGIN_REDIRECT_URL = "/"
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null',)

ALL_CATEGORIES = (
    ('line_follower', _('Line Follower')),
    ('line_follower_junior', _('Line Follower Junior')),
    ('micro_sumo', _('Micro Sumo')),
    ('construction', _('Construction')),
    ('drone', _('Drone')),
    ('stair_climbing', _('Stair Climbing')),
    ('color_selecting', _('Color Selecting')),
    ('scenario', _('Scenario')),
    ('innovative', _('Innovative')),
)

CREATE_CATEGORIES = tuple(ALL_CATEGORIES)
UPDATE_CATEGORIES = tuple(ALL_CATEGORIES)
CONFIRM_CATEGORIES = tuple(ALL_CATEGORIES)
ORDER_CATEGORIES = tuple(ALL_CATEGORIES)
RESULT_CATEGORIES = tuple(ALL_CATEGORIES)

USER_REGISTER = True
USER_UPDATE = True
PROJECT_CREATE = True
PROJECT_UPDATE = True
PROJECT_CONFIRM = True
PROJECT_ORDERS = True
PROJECT_RESULTS = True

SUMO_GROUP_RESULTS = False
SUMO_STAGE_RESULTS = False
SUMO_FINAL_RESULTS= False
SUMO_GROUP_ORDERS = False
SUMO_STAGE_ORDERS = False
SUMO_FINAL_ORDERS= False

# Import local settings
try:
    from local_settings import *
except ImportError:
    pass
