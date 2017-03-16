"""
Django settings for waysily-server project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from usersystem import secrets

import sys
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_ROOT = os.path.join(BASE_DIR, 'djangoapps')
sys.path.insert(0, APPS_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$6(x*g_2g9l_*g8peb-@anl5^*8q!1w)k&e&2!i)t6$s8kia93'

# SECURITY WARNING: don't run with debug turned on in production! It fine in develop
DEBUG = True

TEMPLATE_DEBUG = False
# TODO: Probar quitando * y colocando mi host: www.waysily.com
ALLOWED_HOSTS = ['*']

# A list of origin hostnames that are authorized to make a cross-site HTTP
# request
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    '127.0.0.1:8000',
    'localhost:8080',
    '127.0.0.1:8080',
    'waysily-client-dev.herokuapp.com',
    'https://waysily-client-dev.herokuapp.com',
    'waysily-client-staging.herokuapp.com',
    'https://waysily-client-staging.herokuapp.com',
    'waysily-client-production.herokuapp.com',
    'https://waysily-client-production.herokuapp.com',
    'http://www.waysily.com',
    'www.waysily.com',
    'https://waysily-server-dev.herokuapp.com',
    'https://waysily-server-production.herokuapp.com',
    'https://waysily-server.herokuapp.com',
)

OAUTH2_PROVIDER = {
    # The number of seconds an access token remains valid.
    # RFC6749 Section 4.1.2 recommends a 10 minutes (600 seconds) duration.
    'ACCESS_TOKEN_EXPIRE_SECONDS': 6000
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = secrets.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = secrets.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

SOCIAL_AUTH_FACEBOOK_KEY = secrets.SOCIAL_AUTH_FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = secrets.SOCIAL_AUTH_FACEBOOK_SECRET
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, first_name, last_name, email'
}

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'social.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social.pipeline.user.get_username',

    # Prevents creating a social account with duplicate email
    # to an account already existing in our database.
    'usersystem.pipeline.reject_used_email',

    # Create a user account if we haven't found one yet.
    'social.pipeline.user.create_user',

    # Create the record that associates the social account with the user.
    'social.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social.pipeline.user.user_details',
)

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'utils.api.renderers.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'utils.api.parsers.CamelCaseJSONRenderer',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50
}

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookOAuth2',
)

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'corsheaders',
    'argonauts',
    'usersystem',
    'oauth2_provider',
    'social.apps.django_app.default',
    'rest_framework_social_oauth2',
    'djangoapps.early',
    'djangoapps.locations',
    'djangoapps.profiles',
    'djangoapps.teachers',
    'djangoapps.schools',
    'djangoapps.countries',
    'djangoapps.feedbacks',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'config.urls'

# NOTE: We create a djangoapps/templates in order to storage waysily templates such as: email reset password, verify email, etc.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['djangoapps/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

GRAPPELLI_ADMIN_TITLE = 'Waysily - Administrator'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'waysily_db',
        'USER': 'sergioruizdavila',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# TODO: Comment this block when you will work LOCALLY
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'] = dj_database_url.config()

# TODO: WARNING - Change environment
LOCAL = 'http://localhost:8080'
DEV = 'https://waysily-client-dev.herokuapp.com'
PRD = 'http://www.waysily.com'
STAGING = 'https://waysily-client-staging.herokuapp.com'
# PRD = 'https://waysily-client-production.herokuapp.com'
DOMAIN = LOCAL

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'Etc/GMT-2'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

# TODO: Show in console when you send a email through app
if DOMAIN == LOCAL:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# TODO: Send test email using my gmail account
if DOMAIN == DEV:
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'sergioruizdavila@gmail.com'
    EMAIL_HOST_PASSWORD = 'my-password'
    EMAIL_PORT = 587

# TODO: Send email using my sparkpost - PRD
if DOMAIN == PRD:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.sparkpostmail.com'
    EMAIL_HOST_USER = 'SMTP_Injection'
    EMAIL_HOST_PASSWORD = 'c1506170ad8110344c4ed7436888a74b4c1211aa'
    EMAIL_PORT = 587
    DEFAULT_FROM_EMAIL = 'help@waysily.com'

# NOTE: To allow user resets password is necessary create a new 'Site' on Admin
SITE_ID = 1


"""
DJANGO-REST-AUTH CONFIGURATION
Reference: https://django-allauth.readthedocs.io/en/latest/configuration.html
"""

# The user is required to hand over an e-mail address when signing up.
# TODO: Validar si esto es necesario, ya que esto es una propiedad de django-rest-auth,
# y yo no hago el register con ese plugin.
ACCOUNT_EMAIL_REQUIRED = True

# Choose “optional” or “none” to allow logins with an unverified e-mail address
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# The default protocol used for when generating URLs
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

# Allow verify email after user press link only with a GET request in order to avoid more steps to the user.
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# After user clicked 'confirmation email link', it redirect to main page.
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = DOMAIN
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = DOMAIN

# That adapters is to avoid a exception: add_message() argument must be an HttpRequest object
# reference: http://tech.agilitynerd.com/django-rest-registration-with-django-rest-auth.html
ACCOUNT_ADAPTER = 'main.adapters.MessageFreeAdapter'

# NOTE: the email template: 'email confirmation' is here: /lib/python3.5/site-packages/allauth/templates/
# NOTE: the email template: 'reset password' is here: /lib/python3.5/site-packages/django/contrib/admin/templates/registration

"""--------------------------------------"""

#LOG
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
