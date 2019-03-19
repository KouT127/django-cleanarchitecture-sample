from django.db.models import QuerySet
from rest_framework import serializers
from django_practice.gas_mileages.models import GasMileage
from django_practice.motorcycles.models import Motorcycle
from django_practice.users.models import User


class V1GasMileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasMileage
        fields = ('bike',
                  'user',
                  'id',
                  'amount',
                  'price',
                  'trip',
                  'refill_date',
                  'remark')

    def to_representation(self, instance):
        return dict(
            id=instance.id,
            amount=instance.amount,
            price=instance.price,
            bike=V1MotorcycleSerializer(instance.bike).data
        )


class V1GasMileageSearchSerializer(serializers.ModelSerializer):
    gasMileages = None

    def search(self):
        self.gasMileages = GasMileage.objects.prefetch_related()
        for mileage in self.gasMileages:
            mileage.bike = Motorcycle.objects.get(pk=mileage.bike.id)
        return self


class V1GasMileageResultSerializer(serializers.ModelSerializer):

    def to_representation(self, instance: V1GasMileageSearchSerializer):
        return dict(
            message='ok',
            gasMileages=V1GasMileageSerializer(instance.gasMileages, many=True).data
        )


class V1MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ('manufacturer',
                  'name',
                  'type',
                  'engine_displacement',
                  'model_year')
