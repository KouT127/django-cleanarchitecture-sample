from rest_framework.response import Response
from rest_framework.views import APIView

from django_practice.motorcycles.models import Motorcycle
from django_practice.users.models import User
from django_practice.v1.gas_mileages.serializers import V1GasMileageSearchSerializer, V1GasMileageResultSerializer, \
    V1GasMileageValidationSerializer
from django_practice.v1.motorcycles.serializers import V1MotorcycleSerializer
from django_practice.v1.users.serializers import V1UserSerializer, V1UserResultSerializer


class V1GasMileageView(APIView):

    def get(self, request):
        # ForeignKeyがつくものはManyをつけないとエラー
        serializers = V1GasMileageSearchSerializer()
        obj = serializers.search()
        result = V1GasMileageResultSerializer(obj)
        return Response(result.data)

    def post(self, request):
        user = User.object.first()
        result = V1GasMileageValidationSerializer(request)
        if result.is_valid():
            print(result.validated_data)
            # user.gasmileage_set.add()
            return Response({'message': 'ok'})
        return Response({'message': 'ng'})


class V1UserView(APIView):

    def get(self, request):
        # prefetchはgasmileageのUserIdをIn条件で検索している
        # users = User.object.prefetch_related(Prefetch('gasmileage_set',
        #                                               queryset=GasMileage.objects.all()))

        user = User.object.filter(username__contains='test').first()

        result = V1UserResultSerializer(user)
        return Response(result.data)

    def post(self, request):
        user = User.object.filter(username__contains='test').first()
        bike = Motorcycle.objects.filter(name__contains='R1000').first()
        user.own.add(bike)
        user.save()
        return Response({'succeeded': True})
