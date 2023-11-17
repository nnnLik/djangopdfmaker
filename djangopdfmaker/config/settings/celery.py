import os

from celery import Celery

from .settings import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery(
    "pdfMaker",
    broker_connection_retry_on_startup=True,
)
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

CELERY_BROKER_URL = settings.celery.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = settings.celery.CELERY_RESULT_BACKEND
CELERY_ACCEPT_CONTENT = [
    "application/json",
]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Etc/UTC"
CELERY_ENABLE_UTC = True
