from rest_framework import serializers

from main.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["instance_id", "name", "price", "dc", "model", "brand", "photos"]
