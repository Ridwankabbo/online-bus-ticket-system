from rest_framework import serializers
from .models import (
    Bus,
    Shidule,
    Routes,
    Locations,
    Seats
)

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = "__all__"

class RouteSerializer(serializers.ModelSerializer):
    # location = LocationsSerializer()
    class Meta:
        model = Routes
        fields = "__all__"
        
class ShiduleSerializer(serializers.ModelSerializer):
    route = serializers.PrimaryKeyRelatedField(
        queryset = Routes.objects.all()
    )
    class Meta:
        model = Shidule
        fields = "__all__"
        depth=1
        
class SectsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Seats
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    route=serializers.PrimaryKeyRelatedField(
        queryset = Routes.objects.all()
    )
    shidule = serializers.PrimaryKeyRelatedField(
        queryset = Shidule.objects.all()
    )
    seats = SectsSerializer()
    class Meta:
        model = Bus
        fields = ["id","name", "route", "shidule", "seats"]
        depth=3

