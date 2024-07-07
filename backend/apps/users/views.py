import os
from django.contrib.auth import get_user_model
from rest_framework import status
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from rest_framework.generics import ListCreateAPIView, GenericAPIView, UpdateAPIView
from core.permissions import IsAuthenticatedForGetOrWriteOnly
from rest_framework.response import Response
from apps.users.models import ProfileModel
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from apps.cars.serializers import CarSerializer
from apps.users.serializers import UserSerializer, ProfileAvatarSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)



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

class UserBlockView(GenericAPIView):

    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):

        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnBlockView(GenericAPIView):

    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

class UserAddAvatarView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile:ProfileModel = self.get_object()
        profile.avatar.delete()
        super().perform_update(serializer)
