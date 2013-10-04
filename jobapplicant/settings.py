import os
import platform

CONFIG_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CONFIG_DIR)
PUBLIC_DIR = os.path.join(ROOT_DIR, 'public')

ADMINS = (
    ('Alberto G.', 'alberto.gimenez@pykoder.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'dev': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(ROOT_DIR,'jobapplicant.sqlite'),# Or path to database file if using sqlite3.
        'USER' : '',
        'PASSWORD' : '',
        'HOST' : '',
        'PORT' : ''
    },
    'prod': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jobapplicant',                      # Or path to database file if using sqlite3.
        'USER': 'jobapplicant',                      # Not used with sqlite3.
        'PASSWORD': 'job4dmin',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    },
}

TIME_ZONE = 'America/Asuncion'
LANGUAGE_CODE = 'es-py'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PUBLIC_DIR, 'assets')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(CONFIG_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%0x&amp;q!^q$w7s581pml7x96rei-2wiv(r^%wei=3v*bmani21li'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TP

TEMPLATE_CONTEXT_PROCESSORS = TP + (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'jobapplicant.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'jobapplicant.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'suit',
    'suit_redactor',
    'django.contrib.admin',
    'geoposition',
    'application',
    'candidate',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

if os.name == "nt" or platform.system() == "Darwin":
    DATABASES['default'] = DATABASES['dev']
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG = True
else:
    DATABASES['default'] = DATABASES['prod']
    DEBUG = False

TEMPLATE_DEBUG = DEBUG