from .base import *
from environs import Env

print( "[정보] local settings loaded" )

env = Env()
env.read_env()

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # },
    # "default": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "django-for-beginners",
    #     "USER": "root",
    #     "PASSWORD": "password",
    #     "HOST": "127.0.0.1",
    #     "PORT": "3306",
    # },
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST", "127.0.0.1"),
        "PORT": env("DB_PORT", "3306"),
    }
}