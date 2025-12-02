from rest_framework import serializers
from .models import Booking
from bus.models import Shidule
from user.serializers import UserSerializer
from bus.serializers import BusShiduleSerializer, SeatsSerializer

class BookingSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    shidule = serializers.PrimaryKeyRelatedField(
        queryset=Shidule.objects.all(),
        write_only=True
    )
    seats = serializers.ListField(
        child=serializers.IntegerField(min_value=1, max_value=10)
    )
    class Meta:
        model = Booking
        fields = ['id', 'shidule', 'seats', 'total_amount', 'created_at']
        
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)