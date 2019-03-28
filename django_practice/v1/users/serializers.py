from rest_framework import serializers

from django_practice.users.models import User
from django_practice.v1.motorcycles.serializers import V1MotorcycleSerializer


class V1UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'own'
        )


class V1UserResultSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return dict(
            username=instance.username,
            email=instance.email,
            own=V1MotorcycleSerializer(instance.own.all(), many=True).data
        )
