from rest_framework import serializers
from .models import Booking
from user.serializers import UserSerializer
from bus.serializers import BusShiduleSerializer, SeatsSerializer

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    shidule = BusShiduleSerializer()
    seats = SeatsSerializer()
    class Meta:
        model = Booking
        fields = "__all__"