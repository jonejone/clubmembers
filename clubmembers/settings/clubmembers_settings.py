import dj_database_url
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..'))


# Allow environment variable to turn on debugging
DEBUG = False
if os.environ.get('CLUBMEMBERS_DEBUG'):
    DEBUG = True


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',
    'django_nose',
    'django_countries',
    'registration',

    'clubmembers.members',
    'clubmembers.clubs',
    'clubmembers.frontend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    'clubmembers.clubs.context_processors.club',
)


MIDDLEWARE_CLASSES = (
    'djangotoolbox.sites.dynamicsite.DynamicSiteIDMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'clubmembers.clubs.middleware.ClubMiddleware',
)

DATABASES = {'default': dj_database_url.config()}
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
ROOT_URLCONF = 'clubmembers.frontend.urls'
LANGUAGE_CODE = 'nb_NO'
TIME_ZONE = 'Europe/Oslo'
ACCOUNT_ACTIVATION_DAYS = 30

# Pick up SendGrid config from Heroku environment
if os.environ.get('SENDGRID_USERNAME'):
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

# If we find AWS_ACCESS_KEY_ID, assume usage of S3
# for both static files and media
if os.environ.get('AWS_ACCESS_KEY_ID'):
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_BUCKET_NAME = os.environ['AWS_BUCKET_NAME']
    AWS_BUCKET_URL = 'https://s3.amazonaws.com/%s/' % AWS_BUCKET_NAME
    AWS_QUERYSTRING_AUTH = False
    STATIC_URL = '%sstatic/' % AWS_BUCKET_URL
    MEDIA_URL = '%smedia/' % AWS_BUCKET_URL
    STATICFILES_STORAGE = 'clubmembers.s3utils.StaticRootS3BotoStorage'
    DEFAULT_FILE_STORAGE = 'clubmembers.s3utils.MediaRootS3BotoStorage'

else:
    # Lets use local paths instead of S3
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles/')

ADMINS = (
    ('Jone Eide', 'jone@idev.no'),
)

