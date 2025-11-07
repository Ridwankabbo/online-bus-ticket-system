from django.shortcuts import render
from .models import Bookings
from .serializers import BookingsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["GET","POST"])
def BookingsView(request):
    if request.method == "GET":
        data = Bookings.objects.all()
        serializer = BookingsSerializer(data, many=True)
        
        return Response(serializer.data)
