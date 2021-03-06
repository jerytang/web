"""
Django settings for gaggle project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y*1rpiajd(p=!12uh8nz#4h8ha*dp=$^vo)ippib28d_kz4%#0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'competition',
    'course',
    # dependencies
    'ckeditor',
    'ckeditor_uploader',
    'captcha',
    'crispy_forms',
    'pipeline',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'gaggle.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'user.context_processors.login_form',
            ],
        },
    },
]

WSGI_APPLICATION = 'gaggle.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'data_competition_dev',
        'USER': 'dc',
        'PASSWORD': 'dc',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}

# Redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s:%d/1" % (REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Password
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_URL = 'http://127.0.0.1:8000'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # os.path.join(BASE_DIR, "competition", "static"),
    # os.path.join(BASE_DIR, "user", "static"),
]
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/dc/static/'
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

MEDIA_ROOT = '/var/www/dc/media/'
MEDIA_URL = '/media/'

SUBMISSION_ROOT = '/var/www/dc/submission/'
DATA_ROOT = '/var/www/dc/data/'
TRUTH_ROOT = '/var/www/dc/truth/'

# Function URL
LOGIN_URL = reverse_lazy('user:login')

# Email
# EMAIL_HOST = 'smtp.office365.com'
# EMAIL_HOST_USER = 'hr@biendata.com'
# EMAIL_HOST_PASSWORD = 'xinyu$314'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_FROM = 'support@biendata.com'
# EMAIL_TIMEOUT = 60

EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'npbool_test@163.com'
EMAIL_HOST_SSL = False
EMAIL_PORT = 25
EMAIL_FROM = 'npbool_test@163.com'
EMAIL_TIMEOUT = 60

# CKEditor
CKEDITOR_UPLOAD_PATH = 'competition/'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'width': '100%',
        'toolbar_Custom': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        ],
    }
}

# Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Captcha
CAPTCHA_OUTPUT_FORMAT = u'%(hidden_field)s <div class="captcha-input">%(text_field)s</div> %(image)s'
# Assets
PIPELINE = {
    'PIPELINE_ENABLED': False,
    'COMPILERS': (
        'pipeline.compilers.less.LessCompiler',
    ),
    'CSS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    'STYLESHEETS': {
        'controls': {
            'source_filenames': (
                'css/progress.less',
                'css/tables.less',
                'css/forms.less',
                'css/global.less',
                'css/edit.less'
            ),
            'output_filename': 'css/controls.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
}
