from django.db import models


class UserAutoLotsModel(models.Model):
    class Meta:
        db_table = 'user_auto_lots'

    name = models.CharField(max_length=20)