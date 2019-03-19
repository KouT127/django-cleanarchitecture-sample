from rest_framework.response import Response
from rest_framework.views import APIView

from django_practice.gas_mileages.models import GasMileage
from django_practice.v1.gas_mileages.serializers import V1GasMileageSerializer, V1GasMileageSearchSerializer, \
    V1MotorcycleSerializer, V1GasMileageResultSerializer


class V1GasMileageView(APIView):

    def get(self, request):
        # ForeignKeyがつくものはManyをつけないとエラー
        serializers = V1GasMileageSearchSerializer()
        obj = serializers.search()
        result = V1GasMileageResultSerializer(obj)

        # serializer = V1GasMileageSerializer(self)
        # print(serializer)
        # result = serializer.search()
        # if not serializer.is_valid():
        #     result = V1GasMileageView('NG')
        #     return Response(result.data, status=400)

        # pagination = serializer.search()
        # result = V1GasMileageView(pagination)
        # result.user = self.current_user

        return Response(result.data)
