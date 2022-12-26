import os

from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elasticsearch_stream.settings')

app = Celery("elasticsearch_stream")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
