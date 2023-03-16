from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os


def run():
    User = get_user_model()
    if not User.objects.filter(username=os.getenv('SUPERUSER_NAME')).exists():
        User.objects.create_superuser(
            os.getenv('SUPERUSER_NAME'), os.getenv('SUPERUSER_EMAIL'), os.getenv('SUPERUSER_PASSWORD'))
