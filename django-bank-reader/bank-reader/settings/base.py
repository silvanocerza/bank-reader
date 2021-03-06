import os
import dj_database_url

from getenv import env


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env("DJANGO_DEBUG", False)

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS", "").replace(" ", "").split(",")

# Application definition

INSTALLED_APPS = [
    "scraper",
    "frontend",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "djmoney",
    "rest_framework",
    "django_filters",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bank-reader.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "bank-reader.wsgi.application"

# Limits Django Money currencies
CURRENCIES = ("EUR",)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES_DEFAULT = "postgres://devel:123456@127.0.0.1:5432/bank-reader"
DATABASES = {"default": dj_database_url.config(default=DATABASES_DEFAULT)}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

ASSETS_ROOT = env("DJANGO_ASSETS_ROOT", BASE_DIR)
STATIC_HOST = env("DJANGO_STATIC_HOST", "")

STATIC_URL = STATIC_HOST + "/static/"
STATIC_ROOT = os.path.join(ASSETS_ROOT, "static")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        }
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "standard"},
        "logfile": {
            "class": "logging.FileHandler",
            "filename": BASE_DIR + "/logger.log",
            "formatter": "standard",
        },
    },
    "loggers": {"default": {"handlers": ["console", "logfile"], "propagate": True}},
}

# Settings for Scrapy spiders
SCRAPY_SETTINGS = {
    "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/59.0.3071.115 Safari/537.36",
    "DOWNLOAD_DELAY": 2,
    "CONCURRENT_REQUESTS": 2,
    "DOWNLOADER_MIDDLEWARES": {
        "scrapy_splash.SplashCookiesMiddleware": 723,
        "scrapy_splash.SplashMiddleware": 725,
        "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
    },
    "SPIDER_MIDDLEWARES": {"scrapy_splash.SplashDeduplicateArgsMiddleware": 100},
    "DUPEFILTER_CLASS": "scrapy_splash.SplashAwareDupeFilter",
    "HTTPCACHE_STORAGE": "scrapy_splash.SplashAwareFSCacheStorage",
    "SPLASH_URL": env("SPLASH_URL", "http://localhost:8050/"),
}
