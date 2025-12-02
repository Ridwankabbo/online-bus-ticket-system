from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
# Create your views here.


''' ************************ Create Bookings view *********************** '''
@api_view(['POST'])
def BookingView(request):

    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

