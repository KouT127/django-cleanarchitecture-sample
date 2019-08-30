from rest_framework.utils.serializer_helpers import ReturnList

from django_practice.interface.gateways.repositories.tasks.task_repository import TaskRepository
from django_practice.interface.presenters.task_presenter import TaskPresenter


class TaskInteractor:
    repository: TaskRepository = None
    presenter: TaskPresenter = None

    def __init__(self, repository, presenter):
        self.repository = repository
        self.presenter = presenter

    def get_tasks(self) -> ReturnList:
        tasks = self.repository.find_all_tasks()
        result = self.presenter.respondTasksResult(tasks)
        return result
