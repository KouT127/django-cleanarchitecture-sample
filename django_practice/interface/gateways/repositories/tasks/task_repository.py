from django.db import models
from django.forms.models import model_to_dict

from django_practice.domain.models.task import Task
from django_practice.domain.repositories.task_repository import AbstractTaskRepository
from django_practice.interface.gateways.repositories.tasks.models import TaskModel


class TaskRepository(AbstractTaskRepository):
    def find_by_id(self) -> Task:
        pass

    def find_all(self) -> [Task]:
        task_list = []
        task_models = TaskModel.objects.all()
        for task in task_models:
            task_list.append(Task(id=task.id, title=task.title, description=task.description))
        return task_list
