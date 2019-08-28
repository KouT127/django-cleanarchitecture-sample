from django_practice.interface.gateways.repositories.tasks.task_repository import TaskRepository


class TaskInteractor:
    repository: TaskRepository = None

    def __init__(self, repository):
        self.repository = TaskRepository()

    def get(self):
        self.repository.find_all()
