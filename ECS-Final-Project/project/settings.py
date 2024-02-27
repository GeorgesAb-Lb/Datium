"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import logging
import os
from pathlib import Path
import sys
from urllib.parse import urlparse


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR
 #= os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_re378!*lrw@#6fz8cyfkbl_ts7+s@wl3&pydspmxphuf-kl(&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# import and execute ECS_SETTINGS from environment as python code if they exist

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.humanize',
    'django.contrib.sites',

    'django_extensions',
    'compressor',
    'django_countries',
    #'raven.contrib.django.raven_compat',
    'widget_tweaks',

    'reversion',
    'celery',
    'src.communication',


    'src.users',
    'src.core',
    'src.documents',
    'src.workflow',
    'src.votes',
    'src.checklists',
    'src.authorization',
    'src.meetings',

    'src.tasksv',
    'src.docstash',
    'src.dashboard',
    'src.integration',
    'src.pki',
    'src.notifications',
    'src.tags',
    'src.statistic',
    'src.signature',
    'src.billing',
    'src.boilerplate',
    'src.scratchpad',
    'src.userswitcher',
    'src.bootstrap',
    'src.utils',
    'django_select2',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    #'src.utils.forceauth.ForceAuth',
    #'src.userswitcher.middleware.UserSwitcherMiddleware',
    #'src.pki.middleware.ClientCertMiddleware',
    #'ecs.TestMiddleware',
    #'src.users.middleware.GlobalUserMiddleware',
    'reversion.middleware.RevisionMiddleware',
    #'src.tasksv.middleware.RelatedTasksMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        #'DIRS': [os.path.join(BASE_DIR, 'ecs', 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "src.core.context_processors.ecs_settings",
            ],
        },
    },
]

# WSGI_APPLICATION = "wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "ecs",
        "USER": "postgres",
        'PASSWORD': '12345',
        'PORT': '5432',
        'HOST':'localhost',

    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"

# USE_I18N = True

# USE_TZ = True

TIME_ZONE = 'Europe/Vienna'
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de-AT'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# workaround: we can not use the django gettext function in the settings
# because it depends on the settings.
gettext = lambda s: s

# path where django searches for *.mo files
LOCALE_PATHS = (os.path.join(PROJECT_DIR, "locale"),)

# declare supported languages for i18n. English is the internal project language.
# We do not want to expose our internal denglish to the end-user, so disable english
# in the settings
LANGUAGES = (
    #('en', gettext('English')),
    ('de', gettext('German')),
)

# default site id, some thirdparty libraries expect it to be set
SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = "static/"
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
STATICFILES_DIRS = [
    BASE_DIR/ "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ECS_CA_ROOT = os.path.join(BASE_DIR, '..', 'ecs-ca')


CELERY_IMPORTS = (
    'src.communication.tasks',
    'src.core.tasks',
    'src.core.tests.test_tasks',
    'src.documents.tasks',
    'src.integration.tasks',
    'src.meetings.tasks',
    'src.tasksv.tasks',
    'src.users.tasks',
    'src.votes.tasks',
)
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = (CELERY_TASK_SERIALIZER,)
# try to propagate exceptions back to caller
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
ETHICS_COMMISSION_UUID = 'ecececececececececececececececec'
# if os.getenv('REDIS_URL'):
#     BROKER_URL = os.getenv('REDIS_URL')
#     BROKER_TRANSPORT_OPTIONS = {
#         'fanout_prefix': True,
#         'fanout_patterns': True
#     }
#     CELERY_RESULT_BACKEND = BROKER_URL
#     CELERY_ALWAYS_EAGER = False
# else:
#     # dont use queueing backend but consume it right away
#     CELERY_ALWAYS_EAGER = True
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'


DOMAIN= "localhost"
# ### django_compressor ###
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    (
        'text/x-scss',
        'pyscss -I {} -o {{outfile}} {{infile}}'.format(
            os.path.join(STATIC_ROOT, 'css'))
    ),
)    
if 'ECS_USERSWITCHER_ENABLED' not in locals():
    ECS_USERSWITCHER_ENABLED = True

if not ECS_USERSWITCHER_ENABLED:
    MIDDLEWARE_CLASSES = tuple(item for item in MIDDLEWARE_CLASSES if item != 'src.userswitcher.middleware.UserSwitcherMiddleware')


# registration/login settings
REGISTRATION_SECRET = '!brihi7#cxrd^twvj$r=398mdp4neo$xa-rm7b!8w1jfa@7zu_'
PASSWORD_RESET_SECRET = 'j2obdvrb-hm$$x949k*f5gk_2$1x%2etxhd!$+*^qs8$4ra3=a'

LOGIN_REDIRECT_URL = '/dashboard/'    
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = "/"  # new



DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


CELERY_TIMEZONE = 'Europe/London'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND_UNFILTERED = 'django.core.mail.backends.console.EmailBackend'
EMAIL_UNFILTERED_DOMAINS = ()  # = ('example.com', )
EMAIL_UNFILTERED_INDIVIDUALS = ()  # = ('ada@example.org', 'tom@example.com')

#WSGI_APPLICATION = 'project.wsgi.application'

if os.getenv('SMTP_URL'):
    url = urlparse(os.getenv('SMTP_URL'))
    EMAIL_HOST = url.hostname
    EMAIL_PORT = url.port or 25
    EMAIL_HOST_USER = url.username or ''
    EMAIL_HOST_PASSWORD = url.password or ''

SMTPD_CONFIG = {
    'listen_addr': ('127.0.0.1', 8025),
    'domain': DOMAIN,
    'store_exceptions': False,
}



# Storage Vault settings
STORAGE_VAULT = {
    'dir': os.path.join(PROJECT_DIR, '..', 'ecs-storage-vault'),
    'gpghome' : os.path.join(PROJECT_DIR, '..', 'ecs-gpg'),
    'encryption_uid': 'ecs_mediaserver',
    'signature_uid': 'ecs_authority',
}


# absolute URL prefix w/out trailing slash
ABSOLUTE_URL_PREFIX = "http://"+ DOMAIN+ ":8000"

# directory where to store zipped submission patientinformation and submission form pdfs
ECS_DOWNLOAD_CACHE_DIR = os.path.realpath(os.path.join(PROJECT_DIR, "..", "ecs-cache"))
ECS_DOWNLOAD_CACHE_MAX_AGE = 30 * 24 * 60 * 60  # 30 days




# try to get ECS_VERSION, ECS_GIT_REV from version.py
if not all([k in locals() for k in ['ECS_VERSION', 'ECS_GIT_REV', 'ECS_GIT_BRANCH']]):
    try:
        from version import ECS_VERSION, ECS_GIT_REV, ECS_GIT_BRANCH
    except ImportError:
        ECS_VERSION = 'unknown'
        ECS_GIT_BRANCH = 'unknown'
        ECS_GIT_REV = 'badbadbadbadbadbadbadbadbadbadbadbadbad0'


if os.getenv('ECS_USERSWITCHER_ENABLED'):
    ECS_USERSWITCHER_ENABLED = os.getenv('ECS_USERSWITCHER_ENABLED','').lower() == 'true'

#ECS_DEBUGTOOLBAR = True/False defaults to False if empty
# loads support for django-debug-toolbar

#ECS_WORDING = True/False defaults to False if empty
# activates django-rosetta

# import and execute ECS_SETTINGS from environment as python code if they exist
if os.getenv('ECS_SETTINGS'):
    exec(os.getenv('ECS_SETTINGS'))

# overwrite settings from local_settings.py if it exists
try:
    from src.local_settings import *
except ImportError:
    pass




# https
if 'SECURE_PROXY_SSL' in locals() and SECURE_PROXY_SSL:
  CSRF_COOKIE_SECURE= True
  SESSION_COOKIE_SECURE = True
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# sentry/raven
if 'SENTRY_DSN' in locals():
    import raven
    from raven.transport.threaded_requests import ThreadedRequestsHTTPTransport
    # if no threading support: from raven.transport.requests import RequestsHTTPTransport
    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN,
        'release': ECS_GIT_REV,
        'transport': ThreadedRequestsHTTPTransport,
        'site': DOMAIN,
    }
    SENTRY_CLIENT = 'ecs.utils.ravenutils.DjangoClient'

# user switcher
if 'ECS_USERSWITCHER_ENABLED' not in locals():
    ECS_USERSWITCHER_ENABLED = True

if not ECS_USERSWITCHER_ENABLED:
    MIDDLEWARE_CLASSES = tuple(item for item in MIDDLEWARE_CLASSES if item != 'ecs.userswitcher.middleware.UserSwitcherMiddleware')

# django rosetta activation
if 'ECS_WORDING' in locals() and ECS_WORDING:
    INSTALLED_APPS +=('rosetta',) # anywhere

# django-debug-toolbar activation
if 'ECS_DEBUGTOOLBAR' in locals() and ECS_DEBUGTOOLBAR:
    INSTALLED_APPS += ('debug_toolbar',)
    INTERNAL_IPS = ('127.0.0.1',)

# hack some settings for test and runserver
if 'test' in sys.argv:
    CELERY_ALWAYS_EAGER = True
    INSTALLED_APPS += ('ecs.workflow.tests',)

if 'runserver' in sys.argv:
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
    )