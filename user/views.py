from django.shortcuts import render
from rest_framework.decorators import APIView
from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
)
from rest_framework.response import Response
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()


class UsersView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        
        return Response(serializer.data)


""" 
    =================================
        Registration View
    =================================
"""
class UserRegistrationView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
