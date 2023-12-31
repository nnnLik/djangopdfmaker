import sys

from .settings import settings

DATABASES = {
    "default": {
        "ENGINE": settings.database.DB_ENGINE,
        "NAME": settings.database.DB_NAME,
        "USER": settings.database.DB_USER,
        "PASSWORD": settings.database.DB_PASSWORD,
        "HOST": settings.database.DB_HOST,
        "PORT": settings.database.DB_PORT,
    }
}

if "test" in sys.argv:
    DATABASES = {
        "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
    }
