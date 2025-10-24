from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import(
    Users
)
from .serializer import(
    UsersSerializer,
    UserRegistrationSerializer
)
# Create your views here.


class UsersView(APIView):
    def get(self, request):
        user = Users.objects.all()
        serializer = UsersSerializer(user, many=True)

        return Response(serializer.data)
    
class UserRegistrationView(APIView):
    def post(self, request):
        
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)