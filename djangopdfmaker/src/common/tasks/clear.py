from celery import shared_task

from ..services import services


@shared_task
def cleanup_old_files():
    services.clean_old_files()
