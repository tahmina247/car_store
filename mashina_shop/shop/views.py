from .models import CarMarka, CarModel,Car
from .serializers import CarMarkaSerializer, CarModelSerializer, CarSerializer
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter


class CarMarkaViewSet(viewsets.ModelViewSet):
    queryset = CarMarka.objects.all()
    serializer_class = CarMarkaSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]