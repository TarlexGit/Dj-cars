import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("cars")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "take-date-from-integration": {
        "task": "tasks.take_date_from_integration",
        "schedule": crontab(hour="*/4"),
        "args": ("http://export.maxposter.ru/legocar-used-all/3073-15554.xml",),
    },
    "take-date-from-integration": {
        "task": "tasks.take_date_from_integration",
        "schedule": crontab(hour="*/4"),
        "args": ("http://export.maxposter.ru/legocar-used-all/3413-78456.xml",),
    },
    "take-date-from-integration": {
        "task": "tasks.take_date_from_integration",
        "schedule": crontab(hour="*/4"),
        # Function Arguments
        "args": ("http://kan-ftp.kanavto.ru/newavto/Avtoru_kae_renaultoren.xml",),
    },
}
