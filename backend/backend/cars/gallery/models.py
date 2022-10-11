from django.db import models


class CarImage(models.Model):
    url = models.URLField(null=True, blank=True)
    photo = models.ImageField(upload_to="cars")
