from django.db.models import TextChoices


class CarChoices(TextChoices):
    Hatchback = "Hatchback"
    Sedan = "Sedan"
    Coupe = 'Coupe'
    Crossover = 'Crossover'
    Universal = 'Universal'