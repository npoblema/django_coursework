import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wapubouwy(6458b_!!cm*=bo26bq*#7%$u!dtu+a$_m2yoyhti"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'mailing.apps.MailingConfig',
    # 'users.apps.UsersConfig',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    # "django.middleware.cache.UpdateCacheMiddleware",  # Отключим, пока не установим django-redis
    # "django.middleware.cache.FetchFromCacheMiddleware",  # Отключим, пока не установим django-redis
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("NAME"),
        'USER': os.getenv("USER"),
        'PASSWORD': os.getenv("PASSWORD"),
        'HOST': os.getenv("HOST"),
        'PORT': os.getenv("PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Путь до папки static в вашем проекте
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Аутентификация
AUTH_USER_MODEL = 'users.CustomUser'

# Настройки email (используем Яндекс.Почту, как в рассылках)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# URL для перенаправления после входа/выхода
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'mailing:mailing_list'
LOGOUT_REDIRECT_URL = 'users:home'

# Настройки для подтверждения email
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_METHODS = {'email'}

# Настройки allauth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Настройки шаблонов для allauth
ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSignupForm',
}

# Настройки для восстановления пароля
PASSWORD_RESET_TIMEOUT_DAYS = 1

# Кеширование (временно отключим, пока не установим django-redis)
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/1',  # Локальный Redis, база 1
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'COMPRESSION': True,  # Включаем сжатие для улучшения производительности
#         }
#     }
# }

# Настройки клиентского кеширования
CACHE_MIDDLEWARE_SECONDS = 300  # Кеширование на 5 минут для страниц
CACHE_MIDDLEWARE_KEY_PREFIX = 'django_'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_CACHE_TIMEOUT = 86400  # Кеширование статических файлов на 24 часа

# Настройки для кеширования конкретных вьюх (временно отключим, пока не установим django-redis)
# CACHE_TIMEOUT = 300  # 5 минут для кешируемых вьюх