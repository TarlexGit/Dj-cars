# Generated by Django 4.1.2 on 2022-10-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_car_dc_alter_car_model_alter_car_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="instance_id",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="id"
            ),
        ),
    ]