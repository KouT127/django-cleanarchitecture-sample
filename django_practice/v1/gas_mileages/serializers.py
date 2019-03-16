from rest_framework import serializers

class V1GasMileageSerializer(serializers.ModelSerializer):
    trip = serializers.IntegerField()
    refill_date = serializers.DateField()
