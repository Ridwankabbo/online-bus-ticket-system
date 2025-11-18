from rest_framework import serializers
from .models import (
    Locations,
    Route,
    Bus,
    Seats,
    Shidule
)

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields ='__all__'
        
class RouteSerializer(serializers.ModelSerializer):
    source = LocationsSerializer()
    destination = LocationsSerializer()
    class Meta:
        model = Route
        fields = "__all__"
        
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = "__all__"
        
class SeatsSerializer(serializers.ModelSerializer):
    # bus = BusSerializer()
    class Meta:
        model = Seats
        fields = ["id", "bus", 'seat_name', "seat_status"]
        

class BusShiduleSerializer(serializers.ModelSerializer):
    bus = BusSerializer()
    route = RouteSerializer()
    class Meta:
        model = Shidule
        fields = ["id", "bus", "route", "price", "bus_time"]