from rest_framework import serializers
from .models import Bus_list, Shedule, Bus_seates

class BusShiduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shedule
        fields = "__all__"
        



class BusSerializer(serializers.ModelSerializer):
    
    shidule = BusShiduleSerializer()
    class Meta:
        model = Bus_list
        fields = "__all__"
        depth = 1
        
