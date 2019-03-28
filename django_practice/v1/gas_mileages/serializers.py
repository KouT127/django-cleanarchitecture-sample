from rest_framework import serializers

from django_practice.gas_mileages.models import GasMileage
from django_practice.motorcycles.models import Motorcycle
from django_practice.users.models import User
from django_practice.v1.motorcycles.serializers import V1MotorcycleSerializer


class V1GasMileageSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return dict(
            id=instance.id,
            amount=instance.amount,
            price=instance.price,
            bike=V1MotorcycleSerializer(instance.bike.first()).data,
        )


class V1GasMileageSearchSerializer(serializers.ModelSerializer):
    gasMileages = None
    bike = None

    def search(self):
        # Joinでくっつける
        self.gasMileages = GasMileage.objects.all()
        return self


class V1GasMileageResultSerializer(serializers.ModelSerializer):

    def to_representation(self, instance: V1GasMileageSearchSerializer):
        return dict(
            gasMileages=V1GasMileageSerializer(instance.gasMileages, many=True).data
        )
