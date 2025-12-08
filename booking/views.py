from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
# Create your views here.


''' ************************ Create Bookings view *********************** '''
@api_view(['POST'])
@parser_classes([IsAuthenticated])
def BookingView(request):

    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['POST'])
@parser_classes([IsAuthenticated])
def getBookingsView(request):
    bookings = Booking.objects.filter(user=request.user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

    

