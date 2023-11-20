from config.settings.celery import app

from ..services import services


@app.task()
def cleanup_old_files():
    services.clean_old_files()
