"""
Django settings for something_sunshine project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

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
    's3direct',
    'episodes',
    'smuggler',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'something_sunshine.urls'

WSGI_APPLICATION = 'something_sunshine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# local db setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'something_sunshine',
        'USER': 'jinpark',
        'PASSWORD': 'password1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# AWS keys
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']


# The region of your bucket, more info:
# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region
S3DIRECT_REGION = 'us-east-1'


# Destinations in the following format:
# {destination_key: (path_or_function, auth_test, [allowed_mime_types], permissions, custom_bucket)}
#
# 'destination_key' is the key to use for the 'dest' attribute on your widget or model field
S3DIRECT_DESTINATIONS = {
    # Allow admin users to upload episode audio, tag images, episode thumbnail
    'episode_audio': ('uploads/episodes/audio', lambda u: u.is_superuser, ['audio/mp3', 'audio/mp4', 'audio/ogg', 'audio/x-m4a'], 'public-read',
        AWS_STORAGE_BUCKET_NAME, 'max-age=2592000','attachment'),

    'tag_image': ('uploads/tags/images', lambda u: u.is_superuser, ['image/jpeg', 'image/png', 'image/svg'], 'public-read',
        AWS_STORAGE_BUCKET_NAME, 'max-age=2592000','attachment'),

    'episode_thumbnail': ('uploads/episodes/images', lambda u: u.is_superuser, ['image/jpeg', 'image/jpg', 'image/png', 'image/svg'], 'public-read',
        AWS_STORAGE_BUCKET_NAME, 'max-age=2592000','attachment'),
}

STATIC_BUCKET_URL = "https://static.somethingsunshine.com/"

CORS_ORIGIN_ALLOW_ALL = True
try:
    if os.environ['ENVIRONMENT'] == 'heroku':
        # Parse database configuration from $DATABASE_URL
        import dj_database_url
        DATABASES['default'] =  dj_database_url.config()
        DEBUG = False
        TEMPLATE_DEBUG = False
        SECRET_KEY = os.environ['SECRET_KEY']
    elif os.environ['ENVIRONMENT'] == 'docker':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'postgres',
                'USER': 'postgres',
                'HOST': 'db',
                'PORT': 5432,
            }
        }
        DEBUG = False
        TEMPLATE_DEBUG = False
        SECRET_KEY = os.environ['SECRET_KEY']
except:
    pass
    
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
