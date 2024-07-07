from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import BaseModel
from django.db import models
from apps.users.managers import UserManager
from core.services.upload_avatar import upload_avatar
from django.core import validators as V
from core.enums.regex_enum import RegexEnum


class UserModel(BaseModel, AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[
        V.RegexValidator(*RegexEnum.PASSWORD.value)
    ])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20, validators=[
        V.RegexValidator(*RegexEnum.NAME.value)
    ])
    surname = models.CharField(max_length=20, validators=[
        V.RegexValidator(*RegexEnum.NAME.value)
    ])
    age = models.IntegerField(validators=[
        V.MinValueValidator(15),
        V.MaxValueValidator(150)
    ])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=upload_avatar, blank=True, validators=(
        V.FileExtensionValidator(['gif', 'jpeg', 'png']),
    ))