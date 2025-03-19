import os
from celery import Celery

# Set default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saleor_backend.settings")

app = Celery("saleor_backend")

# Load configuration from settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Autodiscover tasks from installed Django apps
app.autodiscover_tasks()
