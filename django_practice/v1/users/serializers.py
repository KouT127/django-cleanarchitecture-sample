from rest_framework import serializers

from django_practice.users.models import User
from django_practice.v1.motorcycles.serializers import V1MotorcycleSerializer


class V1MessageResultSerializer(serializers.Serializer):
    message = serializers.CharField()

    # def get_initial(self):
    #     return dict(
    #         message='OK',
    #     )

    def to_representation(self, instance: str):
        return dict(
            message=instance,
        )


class V1ErrorMessageResultSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()

    def get_initial(self):
        return dict(
            status=500,
            message='Error',
        )

    def to_representation(self, instance: str):
        return dict(
            status=instance,
            message=instance,
        )


class V1UserResultSerializer(serializers.ModelSerializer):
    own = V1MotorcycleSerializer()

    def to_representation(self, instance):
        result = super.to_representation(instance)
        result['own'] = V1MotorcycleSerializer(instance.own.all(), many=True).data
        return result

    class Meta:
        model = User
        fields = (
            'uuid',
            'username',
            'email',
            'own'
        )


class V1UserValidationSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=False
    )
    email = serializers.CharField(
        required=False
    )
    own = serializers.CharField(
        required=False
    )
