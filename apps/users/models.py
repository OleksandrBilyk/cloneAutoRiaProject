from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import BaseModel
from django.db import models
from apps.users.managers import UserManager
from core.services.upload_avatar import upload_avatar

class UserModel(BaseModel, AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    avatar = models.ImageField(upload_to=upload_avatar, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
