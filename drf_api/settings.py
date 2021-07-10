"""
Django settings for drf_api project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_e!aahx)95vfjdx8)kx_!yb3bnp4n=wpj^=-g5(or!+21_gvil'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # To include support for DEFAULT_AUTHENTICATION_CLASSES, must include this and migrate!
    'rest_framework.authtoken',
    'drf_spectacular',
    'todo.apps.TodoConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Disable the Browsable HTML API
DEFAULT_RENDERER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
)

# Only enable the browseable HTML API in dev (DEBUG=True)
if DEBUG:
    DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + (
        'rest_framework.renderers.BrowsableAPIRenderer',
    )

REST_FRAMEWORK = {
    # Disable the Browsable HTML API UI when in production (DEBUG=False)
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES,

    # Pagination allows you to control how many objects per page are returned
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,

    # The default permission policy may be set globally, using the DEFAULT_PERMISSION_CLASSES setting:
    """
    8 types of permission classes:
    1. AllowAny
    The AllowAny permission class will allow unrestricted access, regardless of if the request was authenticated or unauthenticated.
    This permission is not strictly required, since you can achieve the same result by using an empty list or tuple for the permissions setting, 
    but you may find it useful to specify this class because it makes the intention explicit.

    2. IsAuthenticated
    The IsAuthenticated permission class will deny permission to any unauthenticated user, and allow permission otherwise.
    This permission is suitable if you want your API to only be accessible to registered users.

    3. IsAdminUser
    The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed.
    This permission is suitable is you want your API to only be accessible to a subset of trusted administrators.

    4. IsAuthenticatedOrReadOnly
    The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request. Requests for unauthorised users will only be permitted 
    if the request method is one of the "safe" methods; GET, HEAD or OPTIONS.
    This permission is suitable if you want to your API to allow read permissions to anonymous users, and only allow write permissions to authenticated users.

    5. DjangoModelPermissions
    This permission class ties into Django's standard django.contrib.auth model permissions. This permission must only be applied to views that has a .queryset property set. 
    Authorization will only be granted if the user is authenticated and has the relevant model permissions assigned.

    6. DjangoModelPermissionsOrAnonReadOnly
    Similar to DjangoModelPermissions, but also allows unauthenticated users to have read-only access to the API.

    7. DjangoObjectPermissions
    This permission class ties into Django's standard object permissions framework that allows per-object permissions on models. In order to use this permission class, 
    you'll also need to add a permission backend that supports object-level permissions, such as django-guardian.
    As with DjangoModelPermissions, this permission must only be applied to views that have a .queryset property. Authorization will only be granted if the user is authenticated 
    and has the relevant per-object permissions and relevant model permissions assigned.

    8. TokenHasReadWriteScope
    This permission class is intended for use with either of the OAuthAuthentication and OAuth2Authentication classes, and ties into the scoping that their backends provide.
    """
    # 'DEFAULT_PERMISSION_CLASSES': [
    # 'rest_framework.permissions.AllowAny',
    # 'rest_framework.permissions.IsAuthenticated',
    # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    # 'rest_framework.permissions.DjangoModelPermissions',
    # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    # 'rest_framework.permissions.DjangoObjectPermissions',
    # 'rest_framework.permissions.TokenHasReadWriteScope',
    # ],

    # A list or tuple of authentication classes, that determines the default set of authenticators used when accessing the
    # request.user or request.auth properties.
    # The default authentication schemes may be set globally, using the DEFAULT_AUTHENTICATION_CLASSES setting
    """
    3 types of authentication classes:
    1. BasicAuthentication
    This authentication scheme uses HTTP Basic Authentication, signed against a user's username and password. 
    Basic authentication is generally only appropriate for testing.

    2. SessionAuthentication
    This authentication scheme uses Django's default session backend for authentication. 
    Session authentication is appropriate for AJAX clients that are running in the same session context as your website.

    3. TokenAuthentication
    This authentication scheme uses a simple token-based HTTP Authentication scheme.
    Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.
    To use the TokenAuthentication scheme you'll need to configure the authentication classes to include TokenAuthentication, 
    and additionally include rest_framework.authtoken in your INSTALLED_APPS setting:
    """
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # This authentication scheme uses HTTP Basic Authentication, signed against a user's username and password.
        # Basic authentication is generally only appropriate for testing.
        # 'rest_framework.authentication.BasicAuthentication',

        # This authentication scheme uses Django's default session backend for authentication.
        # Session authentication is appropriate for AJAX clients that are running in the same session context as your website.
        # 'rest_framework.authentication.SessionAuthentication',

        # This authentication scheme uses a simple token-based HTTP Authentication scheme.
        # Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.
        'rest_framework.authentication.TokenAuthentication',
    ),

    # Register DRF_Spectacular AutoSchema with DRF
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# drf-spectacular ships with sane default settings that should work reasonably well out of the box.
# It is not necessary to specify any settings, but we recommend to specify at least some metadata.
SPECTACULAR_SETTINGS = {
    'TITLE': 'Todo API',
    'DESCRIPTION': 'Sample project for testing DRF API',
    'VERSION': '1.0.0',
}

ROOT_URLCONF = 'drf_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drf_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'