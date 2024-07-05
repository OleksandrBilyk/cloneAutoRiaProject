
from rest_framework import serializers

from apps.cars.models import CarModel



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'created_at', 'updated_at')


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'user')
        depth = 1

