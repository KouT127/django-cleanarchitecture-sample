from rest_framework.response import Response
from rest_framework.views import APIView

from django_practice.users.models import User
from django_practice.v1.gas_mileages.serializers import V1GasMileageSearchSerializer, V1GasMileageResultSerializer
from django_practice.v1.motorcycles.serializers import V1MotorcycleSerializer
from django_practice.v1.users.serializers import V1UserSerializer, V1UserResultSerializer


class V1GasMileageView(APIView):

    def get(self, request):
        # ForeignKeyがつくものはManyをつけないとエラー
        serializers = V1GasMileageSearchSerializer()
        obj = serializers.search()
        result = V1GasMileageResultSerializer(obj)
        return Response(result.data)


class V1UserView(APIView):

    def get(self, request):
        # prefetchはgasmileageのUserIdをIn条件で検索している
        # users = User.object.prefetch_related(Prefetch('gasmileage_set',
        #                                               queryset=GasMileage.objects.all()))

        user = User.object.filter(username__contains='test').first()

        result = V1UserResultSerializer(user)
        return Response(result.data)
