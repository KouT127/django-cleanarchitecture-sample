from abc import abstractmethod, ABCMeta

from django_practice.domain.models.task import Task


class AbstractTaskRepository(metaclass=ABCMeta):

    @abstractmethod
    def find_all(self):
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self) -> [Task]:
        raise NotImplementedError()
