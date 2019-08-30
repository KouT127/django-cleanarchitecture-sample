from rest_framework import serializers


class TaskRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
