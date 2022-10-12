from .models import Car
from django.shortcuts import get_object_or_404
from .serializers import CarSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
