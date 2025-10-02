from rest_framework import serializers
from .models import Bus_list
class BusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bus_list
        fields = ['id', 'name', 'form', 'destination', 'price']