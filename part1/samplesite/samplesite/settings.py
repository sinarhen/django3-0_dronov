"""
Django settings for samplesite project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2ctd0)0i&c_4^chln3g-i(1^^gdxa^)u=c9*18*bj90id03dp3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_REFERRER_POLICY = ('no-referrer', 'same-origin')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"  # or same origin
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PHOTO', 'secured')
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bboard.apps.BboardConfig',
    'testapp.apps.TestappConfig',
    'captcha',  # pip install django-simple-captcha
    'precise_bbcode',
    'bootstrap4',
]
BOOTSTRAP4 = {
    'required_css_class': 'required',
    'success_css_class': 'has-success',
    'error_css_class': 'has-error',
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'samplesite.urls'

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
                'bboard.middleware.rubric',
            ],
            'libraries': {
                'filtersandtags': 'bboard.templatetags.filtersandtags'
            }
        },
    },
]

WSGI_APPLICATION = 'samplesite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        "ATOMIC_REQUEST": True,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static/'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
""" LOG IN/OUT DJANGO SUBSYSTEM
LOGIN_URL - On this page redirecting when other page is closed for unauthorized persons 
LOGIN_REDIRECT_URL - On this page redirecting after login
LOGOUT_REDIRECT_URL - On this page redirecting after logout
PASSWORD_RESET_TIMEOUT_DAYS - Number of days which e-mail with reset password option is active
"""

"""
САРТСНА_CНALLENGE_FUNCT - полное имя функции, генерирующей текст для 
    САРТСНА, в виде строки. Поддерживаемые функции перечислены в 
    разд. 1 7.4.2, в описании параметра generator поля CaptchaField. По умолчанию: 
    captcha.helpers.random_char_challenge; 
Глава 1 7. Формы и наборы форм: расширенные инструменты ... 353 
САРТСНА_LENGTH - дпина С АРТ СНА в символах текста. Принимается во внимание только при использовании классической САРТСНА. По умолчанию: 4; 
САРТСНА_МАТН_CНALLENGE_OPERATOR - строка с символом, обозначающим оператор 
    умножения. Принимается во внимание только при использовании математической САРТСНА. По умолчанию: "*". Пример указания крестика в качестве оператора умножения: 
САРТСНА МАТН CНALLENGE OPERATOR = 'х'
CAPTCНA_WORDS_DICTIONARY - полный путь к файлу со словарем, используемым 
    в случае выбора словарной САРТСНА. Словарь должен представлять собой текстовый файл, в котором каждое слово находится на отдельной строке; 
САРТСНА_DICTONARY_MIN_LENGTH - минимальная дпина слова, взятого из словаря, 
    в символах. Применяется в случае выбора словарной САРТСНА. По умолчанию: о; 
САРТСНА_DICTONARY_МАХ_ LENGTH - максимальная дпина слова, взятого из словаря, 
    в символах. Применяется в случае выбора словарной САРТСНА. По умолчанию: 99; 
САРТСНА_TIMEOUT- промежуток времени в минутах, в течение которого сгенерированная САРТСНА останется действительной. По умолчанию: 5; 
САРТСНА_FONT_РАТН - полный путь к файлу шрифта, используемого дпя вывода 
    текста. По умолчанию - путь  <папка , в которой установлен Python>\Lib\sitepackages \captcha\ fonts \Vera . ttf (шрифт Vera, хранящийся в файле по этому 
    пути, является свободным дпя распространения).
CAPTCНA_FONT_SIZE - кегль шрифта текста в пикселах. По умолчанию: 22; 
САРТСНА_LETTER_ROТAТION - диапазон углов поворота букв в тексте САРТСНА 
    в виде кортежа, элементы которого укажут предельные углы поворота в градусах. По умолчанию: (-35, 35) ; 
САРТСНА_FOREGROUND_COLOR - цвет текста на изображении САРТСНА в любом 
    формате, поддерживаемом CSS. По умолчанию: "#001100" (очень темный, практически черный цвет); 
САРТСНА_BACKGROUND_COLOR - цвет фона изображения САРТСНА в любом формате, поддерживаемом CSS. По умолчанию: " # ffffff" (белый цвет); 
CAPTCНA_IМAGE_SIZE - геометрические размеры изображения в виде кортежа, 
    первым элементом которого должна быть ширина, вторым - высота. Размеры 
    исчисляются в пикселах. Если указать None, то размер изображения будет устанавливаться самой библиотекой. По умолчанию - None. 

"""