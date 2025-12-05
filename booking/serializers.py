from rest_framework import serializers
from .models import Booking
from bus.models import Shidule, Seats
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
        seat_numbers = validated_data.pop('seats')
        shidule = validated_data.pop('shidule')
        
        # print(seat_numbers, shidule)
        
        # seleced_bus = Shidule.objects.get(id=shidule)
        # print("selected bus ",shidule.bus.id)
        selectd_bus = shidule.bus.id
        already_booked = Seats.objects.filter(
            bus=selectd_bus,
            seat_name__in = [n for n in seat_numbers],
            seat_status=False
        )
        
        # print("Already booked seats", already_booked)
        
        if already_booked.exists():
            booked_nums = [s.seats_number for s in already_booked]
            raise serializers.ValidationError({
                "seats": f"Seats {', '.join(map(str, booked_nums))} are already exists"
            })
            
        Seats.objects.filter(
            bus = selectd_bus,
            pk__in=[i for i in seat_numbers],
            
        ).update(seat_status=True)
        
        # print("Seats:  ", seats)
        
        booking = Booking.objects.create(
            user = self.context['request'].user,
            shidule = shidule,
            seats = seat_numbers,
            total_amount= shidule.price * len(seat_numbers)
        )
        # print("Bookings: ", booking)
        return booking