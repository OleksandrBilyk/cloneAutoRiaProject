from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from apps.cars.serializers import CarSerializer
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UsersRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UsersAddCarView(GenericAPIView):
    queryset = UserModel.objects.all()

    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_201_CREATED)