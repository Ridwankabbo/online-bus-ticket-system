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
        model = Seats
        fields = ['id','bus','total_seats', "A1",'A2',"B1",'B2',"C1",'C2',"D1",'D2',"E1",'E2']

class BusSerializer(serializers.ModelSerializer):
    route=serializers.PrimaryKeyRelatedField(
        queryset = Routes.objects.all()
    )
    shidule = serializers.PrimaryKeyRelatedField(
        queryset = Shidule.objects.all()
    )
    class Meta:
        model = Bus
        fields = ["id","name", "route", "shidule"]
        depth=3

