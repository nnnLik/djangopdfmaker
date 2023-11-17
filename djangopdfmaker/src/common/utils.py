import uuid

from django.utils import timezone


def generate_unique_filename(instance, filename):
    timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
    unique_id = uuid.uuid4().hex
    return f"html_files/{timestamp}_{unique_id}_{filename}"
