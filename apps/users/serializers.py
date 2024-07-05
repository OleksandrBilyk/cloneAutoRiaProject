from rest_framework import serializers

from apps.cars.serializers import CarSerializer
from apps.users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ("id", "name", "age", "created_at", "updated_at", 'cars')


class UsersWithOutCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', "name")
