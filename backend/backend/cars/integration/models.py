from django.db import models
from .tasks import take_date_from_integration


class DataHub(models.Model):
    title = models.CharField("title", max_length=100)
    url = models.CharField("url", max_length=200)

    def __str__(self) -> str:
        return self.title


# Create your models here.
class Task(models.Model):
    title = models.CharField("title", max_length=100)
    execute = models.BooleanField(default=False)
    result = models.TextField(null=True, blank=True)
    dh = models.ForeignKey(DataHub, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.execute:
            try:
                take_date_from_integration.delay(self.dh.url)
                self.result = "DONE"
                self.execute = False
            except Exception as e:
                self.result = str(e)
        super(Task, self).save(*args, **kwargs)
