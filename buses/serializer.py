from rest_framework import serializers
from .models import (
    Bus,
    Shidule,
    Routes,
    Locations
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
    route = RouteSerializer()
    class Meta:
        model = Shidule
        fields = "__all__"

class BusSerializer(serializers.ModelSerializer):
    # route = RouteSerializer()
    shidule = ShiduleSerializer()
    class Meta:
        model = Bus
        fields = "__all__"
        depth=2

