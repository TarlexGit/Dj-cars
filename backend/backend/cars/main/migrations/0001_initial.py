# Generated by Django 4.1.2 on 2022-10-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена"
                    ),
                ),
                ("dc", models.CharField(max_length=100, verbose_name="дс")),
                ("model", models.CharField(max_length=100, verbose_name="Модель")),
                (
                    "created",
                    models.DateTimeField(blank=True, verbose_name="Дата создания"),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата обновления"
                    ),
                ),
            ],
        ),
    ]
