from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from django_practice.interface.gateways.repositories.tasks.task_repository import TaskRepository
from django_practice.usecase.interactor.task_interactor import TaskInteractor


class V1TaskView(APIView):
    @swagger_auto_schema(operation_summary='',
                         responses={})
    def get(self, request):
        repository = TaskRepository()
        interactor = TaskInteractor(repository)
        test = interactor.get()
        # ForeignKeyがつくものはManyをつけないとエラー
        return Response(dict(), status=200)
