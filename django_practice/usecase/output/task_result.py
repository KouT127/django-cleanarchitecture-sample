from dataclasses import asdict

from rest_framework import serializers

from django_practice.domain.entities.task import Task


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()

    def to_representation(self, instance: Task):
        result = asdict(instance)
        return result


class TaskListSerializer(serializers.ListSerializer):
    child = TaskSerializer()


class TasksResultSerializer(serializers.Serializer):

    def to_representation(self, instance: [Task]) -> dict:
        result = dict(is_succeed=True)
        result['tasks'] = TaskListSerializer(instance).data
        return result
