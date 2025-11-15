from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def BookingView(request):
    booking = Booking.objects.all()
    serializer = BookingSerializer(booking, many=True)
    
    return Response(serializer.data)

    

