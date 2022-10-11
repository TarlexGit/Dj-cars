from django.contrib import admin
from .models import Car, DealerCenter


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dc", "model", "created", "updated")


@admin.register(DealerCenter)
class DealerCenterAdmin(admin.ModelAdmin):
    model = DealerCenter
