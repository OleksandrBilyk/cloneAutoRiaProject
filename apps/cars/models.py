

from core.models import BaseModel
from django.core import validators as V
from django.db import models

from apps.cars.choices import CarChoices
from apps.user_auto_lots.models import UserAutoLotsModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    #     ordering = ('id',)
    #
    # brand = models.CharField(max_length=50, validators=[V.RegexValidator('^[A-Z][a-zA-z\s]{2,49}$', [
    #     'first letter uppercase', 'min 3', 'max 50'])])
    # price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1000000)])
    # year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
    # body_type = models.CharField(max_length=50, choices=[*CarChoices.choices])
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
    body_type = models.CharField(max_length=50)
    auto_lot = models.ForeignKey(UserAutoLotsModel, on_delete=models.CASCADE, related_name='cars')
