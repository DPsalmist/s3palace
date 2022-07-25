import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
SECRET_KEY = 'm_1n^kl^8h+$p3hqro)i@90q4y300t!*j75fon#hp!t=#dw&2e'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.getenv("DEBUG", "False") == "True"
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Default renderer
FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    #'taggit',
    'crispy_forms',
    'payment',
    'payment_app',
    #'paypal.standard.ipn',
    #'django_braintree',
]
'''
# Braintree settings
if (len(sys.argv) >= 2 and sys.argv[1] == 'runserver'):
    BRAINTREE_PRODUCTION = False
else:
    BRAINTREE_PRODUCTION = True
    
BRAINTREE_MERCHANT_ID = 'crcsvnjww9m9p2g2' # Merchant ID
BRAINTREE_PUBLIC_KEY = 'gc66qymjn9cdss92' # Public Key
BRAINTREE_PRIVATE_KEY = '219e6e8564bd4e79a1380c4f5fe7e1ba' # Private key

# Import braintree; make sure you have an account.
import braintree

BRAINTREE_CONF = braintree.Configuration(
braintree.Environment.Sandbox, # change to braintree.Environment.Production in production 
BRAINTREE_MERCHANT_ID,
BRAINTREE_PUBLIC_KEY,
BRAINTREE_PRIVATE_KEY
)
'''
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop2.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = 'BASE_DIR / static'
STATIC_URL = '/static/'
STATICFILES_DIR = 'BASE_DIR /static'
#STATICFILES_DIR = (os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CART_SESSION_ID = 'cart'

#django-paypal settings
PAYPAL_RECEIVER_EMAIL = 'sodbridgesolutions@gmail.com'
PAYPAL_TEST = True
#CYBUJVETWJGW4

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'