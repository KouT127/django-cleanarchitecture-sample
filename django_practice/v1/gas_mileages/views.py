from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework.views import APIView

from django_practice.gas_mileages.models import GasMileage
from django_practice.users.models import User
from django_practice.v1.gas_mileages.serializers import V1GasMileageSerializer, V1GasMileageSearchSerializer, \
    V1MotorcycleSerializer, V1GasMileageResultSerializer


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
        for user in User.object.prefetch_related(Prefetch('gasmileage_set',
                                                          queryset=GasMileage.objects.select_related('user', 'bike'))):
            print(user)
        return Response({'message': 'ok'})
