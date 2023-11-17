from django.db import models


class ContentType(models.TextChoices):
    FILE = "file"
    URL = "url"
