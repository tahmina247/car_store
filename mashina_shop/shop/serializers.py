from rest_framework import serializers
from .models import CarMarka, CarModel, Car

class CarMarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMarka
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_name', 'color', 'year', 'have', 'description']