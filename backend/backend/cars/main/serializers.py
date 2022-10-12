from rest_framework import serializers

from main.models import Car, Brand, DealerCenter, CarModel


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class DealerCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerCenter
        fields = "__all__"


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer()
    brand = BrandSerializer()
    dc = DealerCenterSerializer()

    class Meta:
        model = Car
        fields = ["instance_id", "name", "price", "dc", "model", "brand", "photos"]
