from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from django_practice.interface.gateways.repositories.tasks.task_repository import TaskRepository
from django_practice.interface.presenters.task_presenter import TaskPresenter
from django_practice.usecase.interactor.task_interactor import TaskInteractor


class V1TaskController(APIView):
    @swagger_auto_schema(operation_summary='',
                         responses={})
    def get(self, request):
        repository = TaskRepository()
        presenter = TaskPresenter()
        interactor = TaskInteractor(repository, presenter)
        result = interactor.get_tasks()
        return Response(result, status=200)
