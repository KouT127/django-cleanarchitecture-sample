from django.db import models
from django_practice.motorcycles.models import Motorcycle
from django_practice.users.models import User


class GasMileage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.OneToOneField(Motorcycle, on_delete=models.CASCADE)

    refill_date = models.DateField()

    trip = models.IntegerField()

    amount = models.DecimalField(
        decimal_places=2,
        max_digits=8
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )

    remark = models.TextField(
        blank=True,
        max_length=150,
    )

    def __str__(self):
        return self.user.username + ' ' + self.bike.name
