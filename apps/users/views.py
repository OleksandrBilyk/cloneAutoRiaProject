from django.contrib.auth import get_user_model
from rest_framework import status

from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.cars.models import CarModel

from apps.cars.serializers import CarSerializer
from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)


class UsersAddCarView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)
    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        user_serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_201_CREATED)
