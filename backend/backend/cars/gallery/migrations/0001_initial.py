# Generated by Django 4.1.2 on 2022-10-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarImage",
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
                ("url", models.URLField(blank=True, null=True)),
                ("photo", models.ImageField(upload_to="cars")),
            ],
        ),
    ]