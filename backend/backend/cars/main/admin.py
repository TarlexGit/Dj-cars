from django.contrib import admin
from .models import Car, DealerCenter, Brand, CarModel


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "dc", "brand", "model", "created", "updated")


@admin.register(DealerCenter)
class DealerCenterAdmin(admin.ModelAdmin):
    model = DealerCenter


@admin.register(Brand)
class BrandCenterAdmin(admin.ModelAdmin):
    model = Brand


@admin.register(CarModel)
class CarModelCenterAdmin(admin.ModelAdmin):
    model = CarModel
