
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

    'clubmembers.members',
    'clubmembers.clubs',
    'clubmembers.frontend',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '_db.db',
    }
}

TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
CLUB_ID = 1
ROOT_URLCONF = 'clubmembers.frontend.club_urls'

STATICFILES_DIRS = ('/home/jone/git-repos/bootstrap',)
