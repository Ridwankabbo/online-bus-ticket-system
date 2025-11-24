from django.shortcuts import render
from rest_framework.decorators import APIView, api_view
from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    VerifyOptSerializer,
    UserLoginSerializer,
    ResetPasswordSerializer,
    ForgotPasswordSerializer
)
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from .utils import generate_otp

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
        # data = request.data
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
    
""" 
    ====================================
        Verify otp view
    ====================================
"""    
@api_view(['POST'])
def VerifyOtpView(request):
    serializer = VerifyOptSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        otp = serializer.validated_data.get('otp')
        print(f"email:{email}, otp:{otp}")
        try:
            user = User.objects.get(email=email)
            # print(user)
            if user.otp == otp:
                user.is_active = True
                user.otp=None
                user.save()
                
                return Response({"message":"Otp verified successfully"})
            return Response({"message":"Otp is not valide"})
        except User.DoesNotExist:
            return Response({"message":"User doesn't exist"})
        
    return Response(serializer.errors)

""" 
    ===========================
        Login View
    ===========================
"""
@api_view(['POST'])
def LoginView(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        
        user= authenticate(request, username=email, password=password)
        
        if user is not None:
            if user.is_active:
                print("**************** Login successful ********************")
                return Response({"message":"Login successfull"})
            return Response({"messae":"User isn't actice"})
        return Response({"message":"User isn't registered"})

""" 
    =============================
        Forgot passwod view
    =============================
"""    
@api_view(['POST'])
def ForgotPasswordView(request):
    serializer = ForgotPasswordSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        
        try:
            user = User.objects.get(email=email)
            
            if user is not None:
                user.otp = generate_otp()
                user.save()

                return Response({"message":"New otp send"})
        except User.DoesNotExist:
            return Response({'message':"User doesn't exist"})
    return Response(serializer.errors)
    
""" 
    ==========================
        Reset password view
    ==========================
"""
@api_view(['POST'])    
def ResetPasswordView(request):
    serializer = ResetPasswordSerializer(data= request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        otp = serializer.validated_data.get('otp')
        password = serializer.validated_data.get('password')
        try:
            user = User.objects.get(email=email)
            if user.otp == otp:
                user.set_password(password)
                user.otp=None
                user.save()
            
                return Response({"message":"Password reset successfull"})
        except User.DoesNotExist:
            return Response({"message":"User doesnot exist"})
    return Response(serializer.errors)


""" 
    =========================
        User profile view
    =========================
"""

from .serializers import UserProfileSerializer
from booking.serializers import BookingSerializer
from booking.models import Booking
from rest_framework.permissions import IsAuthenticated
class UserProfileView(APIView):
    
    permission_classes=[IsAuthenticated]
    
    def get(self, request):
        user_profile = request.user
        user_bookings = Booking.objects.get(user=user_profile)
        print(user_bookings)
        serializer = BookingSerializer(user_bookings)
        
        return Response(serializer.data)
    
                
