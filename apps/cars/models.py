from datetime import datetime

from core.models import BaseModel
from django.core import validators as V
from django.db import models
from core.services.upload_pthoto_car import upload_photo_car
from apps.cars.choices import CarChoices
from apps.users.models import UserModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=50, validators=[V.RegexValidator('^[A-Z][a-zA-Z\s]{2,49}$', [
         'first letter uppercase', 'min 3', 'max 50'])])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1000000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
    body_type = models.CharField(max_length=50, choices=[*CarChoices.choices])
    photo_car = models.ImageField(upload_to=upload_photo_car)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
