from rest_framework import serializers

from django_practice.gas_mileages.models import GasMileage
from django_practice.motorcycles.models import Motorcycle
from django_practice.users.models import User
from django_practice.v1.motorcycles.serializers import V1MotorcycleSerializer


class V1GasMileageSerializer(serializers.ModelSerializer):
    # fieldsにbikeを記述をしつつ、V1MotorcycleSerializer()
    # エラーとなるので仕方なくmany=true
    bike = V1MotorcycleSerializer(many=True)

    def to_representation(self, instance):
        # super().to_representation(instance)を使用する場合、ModelSerializerを継承する必要がある。
        result = super().to_representation(instance)
        result['bike'] = V1MotorcycleSerializer(instance.bike.first(), many=False).data
        return result

    class Meta:
        model = GasMileage
        fields = [
            'id',
            'refill_date',
            'trip',
            'amount',
            'price',
            'remark',
            'bike',
        ]


class V1GasMileageSearchSerializer(serializers.Serializer):
    gasMileages = None

    def search(self):
        # Joinでくっつける
        self.gasMileages = GasMileage.objects.all()
        return self


class V1GasMileageResultSerializer(serializers.Serializer):
    # Swagger-API表示用
    gas_mileages = V1GasMileageSerializer()

    def to_representation(self, instance: V1GasMileageSearchSerializer):
        gas_mileages = V1GasMileageSerializer(instance.gasMileages, many=True)
        return dict(
            gas_mileages=gas_mileages.data
        )


class V1GasMileageValidationSerializer(serializers.Serializer):
    bike = serializers.IntegerField()
    refill_date = serializers.DateField()
    trip = serializers.IntegerField()
    amount = serializers.DecimalField(
        decimal_places=2,
        max_digits=8,
    )
    price = serializers.DecimalField(
        decimal_places=2,
        max_digits=8
    )
    remark = serializers.CharField(
        required=False,
        allow_blank=True,
        default='',
        max_length=150,
    )

    def create(self, validated_data):
        user = User.objects.filter(username__contains='admin').first()
        return self.update(instance=GasMileage(user=user), validated_data=validated_data)

    def update(self, instance, validated_data):
        instance.trip = validated_data.get('trip', instance.trip)
        instance.price = validated_data.get('price', instance.price)
        instance.amount = validated_data['amount']
        instance.refill_date = validated_data['refill_date']
        instance.remark = validated_data['remark']
        instance.save()
        return instance
