from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = "admin"
        password = "admin"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, password)
