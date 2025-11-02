from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import (
    Bus,
    Shidule,
    Locations,
    Routes
)
from .serializer import (
    BusSerializer,
    ShiduleSerializer,
    LocationsSerializer,
    RouteSerializer
    
)
# Create your views here.



""" 
    ==============================
        Location Api View
    ==============================
"""
@api_view(["GET", "POST"])
def LocationView(request):
    if request.method == "GET":
        locations = Locations.objects.all()
        serializer = LocationsSerializer(locations, many=True)
        
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = LocationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
    
""" 
    =========================
        Routes Api View 
    =========================
"""
@api_view(["GET", "POST"])
def RouteView(request):
    if request.method == "GET":
        routes = Routes.objects.all()
        serializer = RouteSerializer(routes, many=True)
        
        return Response(serializer.data)

    if request.method == "POST":
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)


""" 
    ===============================
        Shidule Api View
    ===============================
"""
@api_view(["GET", "POST"])
def ShiduleView(request):
    if request.method == "GET":
        shidule = Shidule.objects.all()
        
        serializer = ShiduleSerializer(shidule, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ShiduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
""" 
    =================================
        Bus Api View
    =================================
"""
@api_view(["GET", "POST"])
def BusView(request):
    if request.method == "GET":
        bus = Bus.objects.all()
        serializer = BusSerializer(bus, many=True)
    
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = BusSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)