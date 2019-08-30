from drf_yasg.utils import swagger_auto_schema
from injector import Injector
from rest_framework.response import Response
from rest_framework.views import APIView

from django_practice.usecase.interactor.task_interactor import TaskInteractor


class V1TaskController(APIView):
    @swagger_auto_schema(operation_summary='',
                         responses={})
    def get(self, request):
        injector = Injector()
        interactor = injector.get(TaskInteractor)
        result = interactor.get_tasks()
        return Response(result, status=200)
