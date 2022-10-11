from django.contrib import admin
from .models import CarImage


@admin.register(CarImage)
class DataHubAdmin(admin.ModelAdmin):
    pass
