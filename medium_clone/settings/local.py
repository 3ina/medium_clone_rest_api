from .base import *
from .base import env

SECRET_KEY = env.str("DJANGO_SECRET_KEY",
                     "_3WbuhKOC0_HIq2kFWI5Y0Vg3xMhjVVfOsQua_5WYrbDJbg11fU"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]