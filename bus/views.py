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
        id = request.GET.get('id')
        print("bus id:",id)
        data = Seats.objects.filter(bus__id= id)
        print(data)
        serializer = SeatsSerializer(data, many=True)
    
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = SeatsSerializer(data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
    
""" 
    ==========================
        Shidule list view 
    ==========================
"""
    
@api_view(["GET"])
def BusShiduleList(request):
    shidule_list = Shidule.objects.all()
    
    serializer = BusShiduleSerializer(shidule_list, many=True)
    return Response(serializer.data)


"""
    =======================
        Shidule View
    =======================
"""
@api_view(['GET','POST'])
def BusShiduleView(request):
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    print(source, destination)
    data = Shidule.objects.filter(route__source__name=source, route__destination__name=destination)
    print(data)
    serializer = BusShiduleSerializer(data, many=True)
    return Response(serializer.data)


