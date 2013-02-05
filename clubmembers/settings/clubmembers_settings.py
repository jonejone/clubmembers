import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))

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
    'dynamicsiteslite',

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
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'dynamicsiteslite.middleware.DynamicSitesMiddleware',
    'clubmembers.clubs.middleware.ClubMiddleware',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/jone/git-repos/clubmembers/_db.db',
    }
}

TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
ROOT_URLCONF = 'clubmembers.frontend.club_urls'
LANGUAGE_CODE = 'nb_NO'

STATICFILES_DIRS = ('/home/jone/clubmembers/static',)
LOCALE_PATHS = ('/home/jone/git-repos/clubmembers/conf/locale',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_ACTIVATION_DAYS = 30


SITES_DIR = os.path.join(PROJECT_ROOT, 'sites')
SITES_PACKAGE = 'sites'
DEFAULT_HOST = 'medlemmer.haugalandfrisbee.com'

