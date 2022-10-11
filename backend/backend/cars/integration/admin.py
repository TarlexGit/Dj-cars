from django.contrib import admin

# Register your models here.
from .models import Task, DataHub


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(DataHub)
class DataHubAdmin(admin.ModelAdmin):
    pass
