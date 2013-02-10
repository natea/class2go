import os

from django.conf import settings

# Don't forget to actually create the database named NAME
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

SECRET_KEY = '<REPLACE_ME>'

# Set PRODUCTION to True so we don't show stackdumps on errors
PRODUCTION = False

if PRODUCTION == False:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Set this this to true if you want to show our maint page as root
MAINTENANCE_LANDING_PAGE = False

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
LOGGING_DIR = os.path.join(PROJECT_ROOT, "logs")

# Absolute filesystem path to the directory that will hold user-uploaded files.
# If you upload files from a dev machine, set MEDIA_ROOT to be the root dir for the file
# uploads. If you do this, set in in local_settings.py; not this file.
#Also, if you set it in local_settings.py, don't uncomment the following line as settings.py
#runs after local_settings.py
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# The instance is the group of servers correspond to a C2G stack.  Some good 
# values for this are:
#    "your_name" if you want to stay isolated (thi is the default if missing)
#    "dev" to use the stable dev network util server
#    "stage" or "prod" for something in produciton -- are you sure you want to do that?
INSTANCE="dev"

if INSTANCE != "prod":
    settings.INSTALLED_APPS += (
	'db_test_data',
	'django_nose',
	'django_coverage',
	)

# the APP is so we can support multiple instances of class2go running on the
# same set of servers via apache vhosts.  In dev environments it's safe to just
# use "class2go", this default
APP="class2go"

# Information about this site. Note that the short name here is used to
# build paths to site assets, so is specific and case-sensitive.
SITE_ID = 1
SITE_NAME_SHORT = 'Stanford'
SITE_NAME_LONG = 'Stanford University'
SITE_TITLE = 'Stanford Class2Go'

# Put your name and email address here, so Django serious errors can come to you
# the trailing comma after the list is important so Python correctly interprets 
# this as a list of lists
ADMINS = (
        ('Class2Go Dev', "YOURNAME@stanford.edu"),
        )

# EMAILS
SERVER_EMAIL = 'noreply@class.stanford.edu'
EMAIL_ALWAYS_ACTUALLY_SEND = False

# EMAIL ERROR PINGS
ERROR_SNIPPET_EMAILS = ['YOURNAME@stanford.edu',]


#########
# S3 Storage configuration. Read both stanzas so you understand what these do.
#########
# For using S3 Storage, specify these with real settings. The ACCESS vairables
# are used for authorization to S3 and should be kept secret.
AWS_ACCESS_KEY_ID = 'AAAAAAAAAAAAAAAAAAAA'
AWS_SECRET_ACCESS_KEY = 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'

##
# There are three buckets: STORAGE, SECURE_STORAGE, and RELEASE. STORAGE is
# used for storing public assets and instructor-uploaded material, such as
# downloadable files. SECURE_STORAGE should be configured with a more limited
# set of permissions (allowing download by instructors and not the general
# public), and is used for distributing things like student performance
# reports. RELEASE should be configured with the most limited set of
# permissions, only allowing dowload only from your production (and optionally
# developer) credentials. It is used for the distribution of materials used in
# release and deployment, like custom binaries, secondary authorization tokens,
# etc.
AWS_STORAGE_BUCKET_NAME = 'my-dev-bucket'
AWS_SECURE_STORAGE_BUCKET_NAME = 'my-secure-dev-bucket'
AWS_RELEASE_BUCKET_NAME = 'my-release-dev-bucket'

#Sets the expires parameter in s3 urls to 10 years out.
#This needs to be above the import monkeypatch line
#otherwise we lose the 10 year urls.
AWS_QUERYSTRING_EXPIRE = 3.156e+8

# For using Local storage, set all of these variables to 'local'. You also
# must specify where you want files locally written (see MEDIA_ROOT, below)
##
# AWS_ACCESS_KEY_ID = 'local'
# AWS_SECRET_ACCESS_KEY = 'local'
# AWS_STORAGE_BUCKET_NAME = 'local'
# AWS_SECURE_STORAGE_BUCKET_NAME = 'local'
# AWS_RELEASE_BUCKET_NAME = 'local'
# MEDIA_ROOT = '/opt/class2go/uploads'

if AWS_STORAGE_BUCKET_NAME.count('-') == 1:
    AWS_SECURE_STORAGE_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME.split('-')[0]+'-secure-'+AWS_STORAGE_BUCKET_NAME.split('-')[1]
else:
    AWS_SECURE_STORAGE_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME # If bucket name does not follow our S3 conventions, set secure bucket to be same as bucket

# Setting these variables to 'local' is the idiom for using local storage.
if (AWS_ACCESS_KEY_ID == 'local' or AWS_SECRET_ACCESS_KEY == 'local' or
        AWS_STORAGE_BUCKET_NAME == 'local'):
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

#########
# Celery configuration
#########
# Celery must run for file uploads to work properly and video resizing to take place, etc.
# If you have the above values set to 'local', then set this value to True:
# CELERY_ALWAYS_EAGER = False

# Place where Kelvinator should do its work
# if not specified, then under /tmp, but on Amazon, want to use ephemeral storage
# which is /mnt for some reason
# Generally don't need to set this in dev
# KELVINATOR_WORKING_DIR = '/mnt'

# Place where we should spool uploads.  Django defaults to /tmp, which is fine on
# dev machines, but in AWS we want this to be on ephemeral storage
# FILE_UPLOAD_TEMP_DIR = '/mnt'

# This is if you want to change to a different logging directory than the default,
# which is '/var/log/django/'
# Please keep the trailing '/'
# LOGGING_DIR = '/my/logging/dir/'

CELERY_ACKS_LATE = True
CELERY_IGNORE_RESULT = True   # SQS doesn't support, so this stop lots of spurrious
                              # "*-pidbox" queues from being created

CELERYD_PREFETCH_MULTIPLIER = 1

BROKER_TRANSPORT='sqs'
BROKER_USER = AWS_ACCESS_KEY_ID
BROKER_PASSWORD = AWS_SECRET_ACCESS_KEY
BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-west-2', 
    'queue_name_prefix' : INSTANCE+'-',
    'visibility_timeout' : 3600*6,
}

CELERY_DEFAULT_QUEUE = APP+'-default'
CELERY_DEFAULT_EXCHANGE = APP+'-default'
CELERY_DEFAULT_ROUTING_KEY = APP+'-default'

CELERY_QUEUES = {
    APP+'-default': {'exchange': APP+'-default', 'routing_key': APP+'-default'},
    APP+'-long':    {'exchange': APP+'-long',    'routing_key': APP+'-long'},
}

CELERY_ROUTES = {'kelvinator.tasks.kelvinate': {'queue': APP+'-long', 'routing_key': APP+'-long'},
                 'kelvinator.tasks.resize':    {'queue': APP+'-long', 'routing_key': APP+'-long'},
                 'celerytest.tasks.echo_long': {'queue': APP+'-long', 'routing_key': APP+'-long'},
                }

PIAZZA_ENDPOINT = "https://piazza.com/basic_lti"
PIAZZA_KEY = "class2go"
PIAZZA_SECRET = "piazza_xxxxxxx"

# SMTP INFO for SES -- Amazon Simple Email Service $1 per 10K recipients
SES_SMTP_USER = "USER"
SES_SMTP_PASSWD = "PWD"

#########
# Amazon SES configuration.
#########

# For Production, or if override is set, actually send email
if PRODUCTION or EMAIL_ALWAYS_ACTUALLY_SEND:
    DEFAULT_FROM_EMAIL = SERVER_EMAIL #probably change for production
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = "email-smtp.us-east-1.amazonaws.com"
    EMAIL_PORT = 587
    EMAIL_HOST_USER = SES_SMTP_USER
    EMAIL_HOST_PASSWORD = SES_SMTP_PASSWD
    EMAIL_USE_TLS = True
#Otherwise, send email to a file in the logging directory
else:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = LOGGING_DIR + '/emails_sent.log'

# class2go relies on Youtube pretty heavily. You need to have an API key 
# with youtube application integration enabled
YT_SERVICE_DEVELOPER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
GOOGLE_CLIENT_ID = "NNNNNNNNNNNN.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "YYYYYYYYYYYYYYYYYYYYYYYY"

# Specify this if you want to hit this endpoint to do interactive grading. 
# If left blank, grading has a fallback "localhost" mode with dummy answers.
# GRADER_ENDPOINT = "nnnnnnnnnnnnnnnnnnnn.us-west-2.elb.amazonaws.com"

# Automated grader for CS145
# DB_GRADER_LOADBAL='grade.prod.c2gops.com'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters' : {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s -- %(funcName)s -- line# %(lineno)d : %(message)s '
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'INFO', #making this DEBUG will log _all_ SQL queries.
            'class':'logging.handlers.RotatingFileHandler',
            'formatter':'verbose',
            'filename': LOGGING_DIR+'/'+APP+'-django.log',
            'maxBytes': 1024*1024*500,
            'backupCount': 3,
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        '': {
            'handlers':['mail_admins','logfile', 'console'],
            'propagate': True,
            'level':'DEBUG',
        },
        'django.request': {
            'handlers': ['mail_admins','logfile', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends':{
            'handlers':['logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

LOCAL_CACHE_LOCATION = os.path.join(PROJECT_ROOT, "cache-default")
FILE_CACHE_TIME = 60*60*4    # 4 hours -- files never change
VIDEO_CACHE_TIME = 60*30     # 30 min -- careful of negative caching

CACHES = {
    'file_store': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': LOCAL_CACHE_LOCATION + "/cache-file",
        'TIMEOUT': FILE_CACHE_TIME,
        'OPTIONS': {
            'MAX_ENTRIES': 10000
        }
    },
    'video_store': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': LOCAL_CACHE_LOCATION + "/cache-video",
        'TIMEOUT': VIDEO_CACHE_TIME,
        'OPTIONS': {
            'MAX_ENTRIES': 10000
        }
    },
    'view_store': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': LOCAL_CACHE_LOCATION + "/cache-view",
        'TIMEOUT': 3600,
        'OPTIONS': {
            'MAX_ENTRIES': 10000
            }
    },
    'course_store': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': LOCAL_CACHE_LOCATION + "/cache-course",
        'TIMEOUT': 7200,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
            }
    },
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': LOCAL_CACHE_LOCATION + "/cache-default",
        'TIMEOUT': 3600,
        'OPTIONS': {
            'MAX_ENTRIES': 10000
        }
    },
}