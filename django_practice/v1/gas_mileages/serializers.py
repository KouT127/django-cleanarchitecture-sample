from django.db.models import QuerySet
from rest_framework import serializers
from django_practice.gas_mileages.models import GasMileage
from django_practice.motorcycles.models import Motorcycle
from django_practice.users.models import User


class V1GasMileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasMileage
        fields = ('bike', 'id', 'amount',)

    def to_representation(self, instance):
        bike = Motorcycle.objects.all()
        bike_serializer = V1MotorcycleSerializer(bike, many=True)
        return dict(
            refill_date=instance.refill_date,
            amount=instance.amount,
            bike=bike_serializer.data,
        )


class V1GasMileageSearchSerializer(serializers.ModelSerializer):
    gasMileages = None
    bike = None

    def search(self):
        self.gasMileages = GasMileage.objects.filter(
            user__uuid='5ee0a92d-74ae-4753-a416-56487627ca74').prefetch_related()
        # self.bike = Motorcycle.objects.filter(gasmileage__in=self.gasMileages)
        return self


class V1MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ('manufacturer', 'name')
