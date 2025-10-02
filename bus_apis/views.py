from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bus_list
from .serializer import BusSerializer
# Create your views here.

@api_view(['GET'])
def getBusList(request):
    
    if request.method == "GET":
        obj = Bus_list.objects.all()
        
        serializer = BusSerializer(obj, many=True)

        return Response(serializer.data)

