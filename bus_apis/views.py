from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Bus_list
from .serializer import BusSerializer
# Create your views here.

# @api_view(['GET'])
# def getBusList(request):
    
#     if request.method == "GET":
#         obj = Bus_list.objects.all()
        
#         serializer = BusSerializer(obj, many=True)

#         return Response(serializer.data)


#............... Create a class based API view using ListAPIView .............................

class BusSearchAPIView(ListAPIView):
    
    serializer_class = BusSerializer
    
    def get_queryset(self):
    
        queryset = Bus_list.objects.all()
        
        from_location = self.request.query_params.get('from_location')
        destination_location = self.request.query_params.get('destination')
        
        # print(from_location)
        
        if from_location is not None:
            queryset = queryset.filter(from_location = from_location)
        if destination_location :
            queryset = queryset.filter(destination = destination_location)
            
        return queryset

