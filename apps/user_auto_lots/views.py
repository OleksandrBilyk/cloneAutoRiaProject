from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.cars.serializers import CarSerializer
from apps.user_auto_lots.models import UserAutoLotsModel
from apps.user_auto_lots.serializers import AutoLotsSerializer


class AutoLotsListCreateView(ListCreateAPIView):
    queryset = UserAutoLotsModel.objects.all()
    serializer_class = AutoLotsSerializer


class AutoParkAddCarView(GenericAPIView):
    queryset = UserAutoLotsModel.objects.all()

    def post(self, *args, **kwargs):
        auto_lot = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_lot=auto_lot)
        ap_serializer = AutoLotsSerializer(auto_lot)
        return Response(ap_serializer.data, status.HTTP_201_CREATED)
