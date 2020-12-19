from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINS_MODULE", "programming_test.settings")
app = Celery("programming_test")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()