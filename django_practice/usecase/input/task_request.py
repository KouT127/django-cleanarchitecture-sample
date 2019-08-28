from rest_framework import serializers


class TaskRequest(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
