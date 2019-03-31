from django.db import models
from django.db.models.manager import BaseManager


class MotorcycleManager(models.Manager):
    pass


class Motorcycle(models.Model):
    objects = MotorcycleManager()
    SCOUTER = 'sc'
    BIG_SCOUTER = 'bs'
    SUPER_SPORTS = 'ss'
    OFFROAD = 'of'

    MOTORCYCLE_TYPES = (
        (SCOUTER, 'Scouter'),
        (BIG_SCOUTER, 'Big_Scouter'),
        (SUPER_SPORTS, 'Super_Sport'),
        (OFFROAD, 'Offroad'),
    )

    YAMAHA = 'ya'
    HONDA = 'ho'
    KAWASAKI = 'ka'
    SUZUKI = 'su'

    MANUFACTURERS = (
        (YAMAHA, 'YAMAHA'),
        (HONDA, 'HONDA'),
        (KAWASAKI, 'KAWASAKI'),
        (SUZUKI, 'SUZUKI'),
    )

    manufacturer = models.CharField(
        max_length=20,
        choices=MANUFACTURERS,
    )

    name = models.CharField(
        max_length=30,
    )

    type = models.CharField(
        max_length=2,
        choices=MOTORCYCLE_TYPES,
    )

    engine_displacement = models.IntegerField()

    model_number = models.CharField(
        max_length=20
    )

    model_year = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
