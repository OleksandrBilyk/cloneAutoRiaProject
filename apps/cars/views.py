from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filters import car_filter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer, CarListSerializer


class CarListView(ListAPIView):
    # queryset = CarModel.objects.all()
    serializer_class = CarListSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params.dict())



class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

