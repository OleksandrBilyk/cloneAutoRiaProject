from rest_framework import serializers

from apps.cars.serializers import CarSerializer
from apps.user_auto_lots.models import UserAutoLotsModel


class AutoLotsSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = UserAutoLotsModel
        fields = ('id', 'name', 'cars')