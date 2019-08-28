from django.db import models
from django.forms.models import model_to_dict

from django_practice.domain.models.task import Task
from django_practice.interface.gateways.repositories.tasks.models import TaskModel


class TaskRepository:
    def find_by_id(self) -> Task:
        pass

    def find_all(self) -> [Task]:
        task_list = []
        task_models = TaskModel.objects.all()
        for task in task_models:
            task_list.append(Task(model_to_dict(task)))
        return task_list
