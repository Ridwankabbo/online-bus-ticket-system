from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Locations,
    Route,
    Locations,
    Bus,
    Seats,
    Shidule
)
from .serializers import (
    BusShiduleSerializer,
    LocationsSerializer,
    SeatsSerializer
)
# Create your views here.

"""
    ===========================
        Location view
    ===========================
"""
@api_view(['GET'])
def LocationView(request):
    data = Locations.objects.all()
    serialize = LocationsSerializer(data, many=True)
    
    return Response(serialize.data)

"""
    =============================
        Bus seats view
    =============================
"""
@api_view(['GET', "PATCH"])
def BusSeatsView(request):
    if request.method == "GET":
        data = Seats.objects.all()
        serializer = SeatsSerializer(data, many=True)
    
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = SeatsSerializer(data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)


"""
    =======================
        Shidule View
    =======================
"""
@api_view(['GET'])
def BusShiduleView(request):
    data = Shidule.objects.all()
    serializer = BusShiduleSerializer(data, many=True)
    return Response(serializer.data)


