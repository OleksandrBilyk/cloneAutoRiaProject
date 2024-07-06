from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer, CarListSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarListSerializer
    filterset_class = CarFilter




class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

