import ConfigParser
import djcelery
import os
import sys


SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
config = ConfigParser.ConfigParser()
config.read(os.path.join(SETTINGS_DIR, "../../boiler_plate.ini"))
config_file = os.path.join(SETTINGS_DIR, "../../local_settings.ini")
if os.path.isfile(config_file):
    config.read(config_file)

DEBUG = True if int(config.get('debug', 'django', 0)) == 1 else False
TEMPLATE_DEBUG = DEBUG
ADMINS = (('Mark Litwintschik', 'mark@marksblogg.com'),)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': config.get('db', 'engine', 
            'django.db.backends.sqlite3'),
        'NAME': config.get('db', 'name', 'backbone-directory.sqlite'),
        'USER': config.get('db', 'user', ''),
        'PASSWORD': config.get('db', 'pass', ''),
        'HOST': config.get('db', 'host', ''),
        'PORT': '',
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'backbone-directory-test.sqlite'
    }

TIME_ZONE = config.get('locale', 'time_zone', 'UTC')
LANGUAGE_CODE = config.get('locale', 'language_code', 'en-gb')
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(SETTINGS_DIR, '../../assets')
MEDIA_URL = config.get('amazon_cloudfront', 'http_url', '')
ADMIN_TOOLS_MEDIA_URL = config.get('amazon_cloudfront', 'http_url', '')
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '*kv2r4g8kq)6x%vs!69y5881w$*x$w=o!8pm2*=4%fjoz2qeo&amp;'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'base.urls'
WSGI_APPLICATION = 'base.wsgi.application'
TEMPLATE_DIRS = (os.path.join(SETTINGS_DIR, '../templates'),)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'gunicorn',
    'south',
    'tastypie',
    'api',
    'home',
)

CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = 10
CELERY_RESULT_BACKEND = 'amqp'
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
BROKER_URL = config.get('amqp', 'broker_url', '')

djcelery.setup_loader()

if 'test' in sys.argv:
    # See https://github.com/celery/django-celery/issues/149
    SOUTH_MIGRATION_MODULES = {'djcelery': 'ignore'}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.' + 
        'ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s ' + 
                '%(process)d %(thread)d %(message)s',
            'datefmt': '%a, %d %b %Y %H:%M:%S %z',
        },
        'simple': {
            'format': '[%(levelname)s] %(asctime)s - %(message)s',
            'datefmt': '%a, %d %b %Y %H:%M:%S %z',
        },
        'django-default-verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s ' + 
                '%(process)d %(thread)d %(message)s'
        },
        'common-logging-v2': {
            'format': '[%(asctime)s] - %(message)s',
            'datefmt': '%d/%b/%Y:%H:%M:%S %z',
        },
        'parsefriendly': {
            'format': '[%(levelname)s] %(asctime)s - M:%(module)s, ' + 
                'P:%(process)d, T:%(thread)d, MSG:%(message)s',
            'datefmt': '%d/%b/%Y:%H:%M:%S %z',
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'watched-log-file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'parsefriendly',
            'filename': config.get('logging', 'log_file', 
                '/tmp/backbone-directory-backend.log'), 
            'mode': 'a',
        },
    },
    'loggers': {
        'backend': {
            'level': 'DEBUG',
            'handlers': ['watched-log-file', 'console'],
            'propagate': False,
        },
    }
}