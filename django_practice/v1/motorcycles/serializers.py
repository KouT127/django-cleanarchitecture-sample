from rest_framework import serializers

from django_practice.motorcycles.models import Motorcycle


class V1MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ('manufacturer',
                  'name',
                  'type',
                  'engine_displacement',
                  'model_year')
