from django_practice.interface.gateways.repositories.tasks.task_repository import TaskRepository


class TaskInteractor:
    repository: TaskRepository = None

    def __init__(self, repository):
        self.repository = repository

    def get(self):
        return self.repository.find_all()
