# Django settings for Class2Go project.
from os import path

import django.template
import djcelery

import monkeypatch

#ADDED FOR url tag future
django.template.add_to_builtins('django.templatetags.future')
#Added for celery
djcelery.setup_loader()

# the INSTANCE should be "prod" or "stage" or something like that
# if it hasn't been set then get the user name
# since we use this for things like queue names, we want to keep this unique
# to keep things from getting cross wired
try:
    from os import getuid
    from pwd import getpwuid
    INSTANCE=getpwuid(getuid())[0]
except:
    INSTANCE="unknown"

# the APP is so we can support multiple instances of class2go running on the
# same set of servers via apache vhosts.  In dev environments it's safe to just
# use "class2go", this default
APP="class2go"

# If PRODUCTION flag not set in local_settings.py, then set it now.
#PRODUCTION = True

PRODUCTION = True
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'class2go',                      # Or path to database file if using sqlite3.
        'USER': 'class2go',                      # Not used with sqlite3.
        'PASSWORD': 'class2go',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'readonly': {                        # optional section, DB to use for reporting
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': '',                      
        'USER': '',                      
        'PASSWORD': '',                  
        'HOST': '',                      
        'PORT': '',                      
     },        
    'celery': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'celerydb.sqlite',
    },

}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'


# These site variables are used for display in the product and can 
# drive any conditional changes (display, etc).
# Override all four in your local_settings.py file, otherwise they will 
# default back to Stanford.

SITE_ID = 1
SITE_NAME_SHORT = 'Stanford'
SITE_NAME_LONG = 'Stanford University'
SITE_TITLE = 'Stanford Class2Go'

# ADMINS should be set in local_settings.py too.
ADMINS = (
        ('Class2Go Dev', "YOURNAME@stanford.edu"),
        )

MANAGERS = ADMINS

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# If you upload files from a dev machine, set MEDIA_ROOT to be the root dir for the file
# uploads. If you do this, set in in local_settings.py; not this file.
#Also, if you set it in local_settings.py, don't uncomment the following line as settings.py
#runs after local_settings.py
#MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/opt/' + APP + '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'convenience_redirect.redirector.convenience_redirector',
    'courses.common_page_data_middleware.common_data',
    'courses.user_profiling_middleware.user_profiling',
    'exception_snippet.midware.error_ping',

)

ROOT_URLCONF = 'urls'


### CACHING ###
# config info here: see https://docs.djangoproject.com/en/dev/topics/cache

LOCAL_CACHE_LOCATION = "/opt/class2go"

thispath = path.dirname(path.realpath(__file__))
TEMPLATE_DIRS = (
    thispath+'/templates'
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'context_processor.context_settings'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'registration',
    'south',
    'djcelery',
    #'kombu.transport.django',
    'c2g',
    'courses',
    'courses.forums',
    'courses.announcements',
    'courses.videos',
    'courses.video_exercises',
    'courses.email_members',
    'courses.reports',
    'problemsets',
    'django.contrib.flatpages',
    'storages',
    'celerytest',
    'kelvinator',
    'db_scripts',
    'convenience_redirect',
    'exception_snippet',
    'rest_framework',
    #'reversion',
    'certificates',
                      )
if INSTANCE != "prod":
    INSTALLED_APPS += (
                        'db_test_data',
                        'django_nose',
                        'django_coverage',
                       )


MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Storage

# By default we use S3 storage.  Make sure we have the settings we need.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


#This states that app c2g's UserProfile model is the profile for this site.
AUTH_PROFILE_MODULE = 'c2g.UserProfile'

ACCOUNT_ACTIVATION_DAYS = 7 #used by registration


# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# If PRODUCTION flag not set in local_settings.py, then set it now.
LOGGING_DIR = '/var/log/django/'

USE_ETAGS = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Session Settings
SESSION_COOKIE_AGE = 3*30*24*3600


# Database routing
DATABASE_ROUTERS = ['c2g.routers.CeleryDBRouter',
                    'c2g.routers.ReadonlyDBRouter',
                   ]

# Actually send email
EMAIL_ALWAYS_ACTUALLY_SEND = False

# Email Settings
SERVER_EMAIL = 'noreply@class.stanford.edu'

#Max number of emails sent by each worker, defaults to 10
#EMAILS_PER_WORKER = 10


# Testing related settings
# Set a specific testrunner to use
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--config=./nose.cfg']

# we use django_coverage for test coverage reports. Configure here.
COVERAGE_ADDITIONAL_MODULES = ['accounts', 'kelvinator']
COVERAGE_MODULE_EXCLUDES = ['tests$', 'settings$', 'urls$', 'locale$',
                            'common.views.test', '__init__', 'django',
                            'migrations', 'south', 'djcelery']
COVERAGE_REPORT_HTML_OUTPUT_DIR = './coverage-report/'
COVERAGE_CUSTOM_REPORTS = False

# Automated grader for CS145
DB_GRADER_LOADBAL='grade.prod.c2gops.com'

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from local_settings import *
except ImportError:
    pass
