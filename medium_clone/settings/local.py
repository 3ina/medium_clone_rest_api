from .base import *
from .base import env

SECRET_KEY = env.str("DJANGO_SECRET_KEY",
                     "_3WbuhKOC0_HIq2kFWI5Y0Vg3xMhjVVfOsQua_5WYrbDJbg11fU"
                     )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@medium.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Medium"
