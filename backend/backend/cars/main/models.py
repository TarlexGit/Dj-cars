from tabnanny import verbose
from django.utils import timezone
from django.db import models
from gallery.models import CarImage


class DealerCenter(models.Model):
    """Дилерские центры"""

    name = models.CharField("Название", max_length=100)
    address = models.CharField("Адрес", max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    """Бренд или марка авто"""

    name = models.CharField("Название", max_length=100)

    def __str__(self) -> str:
        return self.name


class CarModel(models.Model):
    """Модели авто"""

    name = models.CharField("Название", max_length=100)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):

    instance_id = models.CharField("id", max_length=100, null=True, blank=True)
    name = models.CharField("Название", max_length=100, null=True, blank=True)
    price = models.DecimalField(
        "Цена", max_digits=10, decimal_places=2, null=True, blank=True
    )
    dc = models.ForeignKey(
        DealerCenter, on_delete=models.CASCADE, null=True, blank=True
    )
    model = models.ForeignKey(
        CarModel, verbose_name="Модель", on_delete=models.CASCADE, null=True, blank=True
    )
    brand = models.ForeignKey(
        Brand, verbose_name="Бренд", on_delete=models.CASCADE, null=True, blank=True
    )
    created = models.DateTimeField("Дата создания", blank=True)
    updated = models.DateTimeField("Дата обновления", null=True, blank=True)

    integration_url = models.CharField(
        "integration_url", max_length=150, null=True, blank=True
    )
    photos = models.ManyToManyField(CarImage, verbose_name="Фотки", blank=True)

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
            self.updated = None
        elif self.created and self.updated is None:
            self.updated = timezone.now()
        super(Car, self).save(*args, **kwargs)
