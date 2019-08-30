from abc import abstractmethod, ABCMeta

from django_practice.domain.entities.task import Task


class AbstractTaskRepository(metaclass=ABCMeta):

    @abstractmethod
    def find_all_tasks(self):
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self) -> [Task]:
        raise NotImplementedError()
