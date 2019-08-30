from django_practice.domain.entities.task import Task
from django_practice.usecase.output.task_result import TasksResultSerializer


class TaskPresenter:
    def respondTasksResult(self, tasks: [Task]) -> dict:
        return TasksResultSerializer(tasks).data
