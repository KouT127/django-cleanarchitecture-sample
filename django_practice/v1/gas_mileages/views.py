from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt import authentication

from django_practice.motorcycles.models import Motorcycle
from django_practice.users.models import User
from django_practice.v1.gas_mileages.serializers import V1GasMileageSearchSerializer, V1GasMileageResultSerializer, \
    V1GasMileageValidationSerializer
from django_practice.v1.users.serializers import V1UserResultSerializer


class V1GasMileageView(APIView):
    authentication_classes = (authentication.JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        print(request.user)
        # ForeignKeyがつくものはManyをつけないとエラー
        serializers = V1GasMileageSearchSerializer()
        obj = serializers.search()
        result = V1GasMileageResultSerializer(obj)
        return Response(result.data)

    def post(self, request):
        user = User.object.first()
        User.objects.first()
        result = V1GasMileageValidationSerializer(data=request.data)
        if result.is_valid():
            print(result.validated_data)
            motorcycle_name = result.validated_data['motorcycle_name']
            bike = Motorcycle.objects.filter(name__contains=motorcycle_name).first()
            print(bike)
            admin: User = User.objects.filter(username__contains='admin').first()
            admin.gasmileage_set.add()
            # user.gasmileage_set.add()
            return Response({'message': 'ok'})
        print(result.errors.__str__())
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
