import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

BASE_DIR = Path(__file__).resolve().parent.parent

# ================================
# SECURITY & ENVIRONMENT SETTINGS
# ================================
SECRET_KEY = os.getenv("SECRET_KEY")  # Read from Render environment
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    "shreshta-backend.onrender.com",  # specific render domain
    ".onrender.com",                   # allow all render subdomains
    "localhost",
    "127.0.0.1",
] + [host for host in os.getenv("ALLOWED_HOSTS", "").split(",") if host]

# ====================
# INSTALLED APPS
# ====================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'corsheaders',
    'rest_framework',

    # Your apps
    'accounts',
]

# ====================
# MIDDLEWARE
# ====================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "firstbackend.urls"

# ====================
# TEMPLATES
# ====================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "firstbackend.wsgi.application"

# ====================
# DATABASE (SQLite)
# ====================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ====================
# PASSWORD VALIDATION
# ====================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ====================
# INTERNATIONALIZATION
# ====================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =====================
# STATIC & MEDIA FILES
# =====================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = []

# WhiteNoise configuration for static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ====================
# DEFAULT PRIMARY KEY
# ====================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"