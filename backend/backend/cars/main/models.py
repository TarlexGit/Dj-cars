from django.utils import timezone
from django.db import models


class DealerCenter(models.Model):
    """Дилерские центры"""

    name = models.CharField("Название", max_length=100)
    address = models.CharField("Адрес", max_length=100)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    name = models.CharField("Название", max_length=100)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    dc = models.ForeignKey(DealerCenter, on_delete=models.CASCADE)
    model = models.CharField("Модель", max_length=100)
    created = models.DateTimeField("Дата создания", blank=True)
    updated = models.DateTimeField("Дата обновления", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
            self.updated = None
        elif self.created and self.updated is None:
            self.updated = timezone.now()
        super(Car, self).save(*args, **kwargs)


class Brand(models.Model):
    """Бренд или марка авто"""

    name = models.CharField("Название", max_length=100)


class CarModel(models.Model):
    """Модели авто"""

    name = models.CharField("Название", max_length=100)
