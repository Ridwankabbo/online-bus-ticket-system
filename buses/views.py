from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from .models import (
    Bus,
    Shidule,
    Locations,
    Routes,
    Seats
)
from .serializer import (
    BusSerializer,
    ShiduleSerializer,
    LocationsSerializer,
    RouteSerializer,
    SectsSerializer
    
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
""" 
    ===========================
        Search Bus View
    ===========================
"""
@api_view(["GET", "POST"])
def SearchBusView(request):
    if request.method == "POST":
        from_place_name = request.POST.get('fromplace')
        dest_place_name = request.POST.get('destplace')
        # print(from_place_name, dest_place_name)

        try:
            # 1. Retrieve Location instances (Dhaka, Chittagong, etc.)
            # This is correct and gives you the Location objects
            from_location = get_object_or_404(Locations, name__iexact=from_place_name)
            dest_location = get_object_or_404(Locations, name__iexact=dest_place_name)
            # print(from_location, dest_location)

            # 2. Filter Bus using the Location instances through the Route foreign key
            buses = Bus.objects.filter(
                # Correctly links Bus -> Route -> Location instance
                route__destination_from=from_location, 
                route__destination_to=dest_location
            )
            
            if buses.exists():
                serializer = BusSerializer(buses, many=True)
                return Response(serializer.data)
            return Response({"message":"Bus doesn't exist"})
            
        except Exception as e:
            # Check the exact line where e is raised if the error persists.
            # If the error is still a 500, it's occurring inside the filter().
            return Response({"message":f"Error occured {e}"})
        
""" 
    =========================
        Seats View
    =========================
"""        
@api_view(['GET', 'POST'])
def SeatsView(request):
    if request.method == "POST":
        # data = request.body
        bus_id = request.data.get('bus_id')
        print(bus_id)
        
        try:
            seats = Seats.objects.get(bus=bus_id)
            serializer = SectsSerializer(seats)
            
            return Response(serializer.data)
        except Seats.DoesNotExist:
            return Response({"message":"Doesn't exist"})
        
   
        