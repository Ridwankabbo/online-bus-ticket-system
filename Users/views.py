from django.shortcuts import render
from rest_framework.decorators import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .utils import generate_otp
# from .models import(
#     Users
# )
from .serializer import(
    UsersSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
    VerifyUserOtpSerializer,
    ResendOtpSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer
)
# Create your views here.

User = get_user_model()

""" 
    =======================
        All users view
    =======================
"""

class UsersView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UsersSerializer(user, many=True)

        return Response(serializer.data)
    
    
""" 
    ============================
        Registration View
    ============================
"""
    
class UserRegistrationView(APIView):
    def post(self, request):
        
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors)
    
""" 
    ============================
        Login View
    ============================
"""
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            
            print(f"email:{email} password:{password}")
            
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                if user.is_active:
                    print("**************************** Login successfull **************************")
                    return Response({"message":"Login successfull"})
                return Response({"message":"User is't active"})
            return Response({"message":"User is't registered"})
        

class VerifyOtpView(APIView):
    def post(self, request):
        serializer = VerifyUserOtpSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            otp = serializer.validated_data.get('otp')
            
            try:
                user = User.objects.get(email=email)
                print(user)
                
                if user.otp == otp:
                    user.is_active = True
                    user.otp = None
                    user.save()
                
                    return Response({"message":"Verification successfull"})
            except User.DoesNotExist:
                return Response({"message":"User doesn't exist"})
        return Response(serializer.errors)
    
class ResendOtpView(APIView):
    def post(self, request):
        serializer = ResendOtpSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            
            user = User.objects.get(email = email)
            
            if user is not None:
                new_otp = generate_otp()
                user.otp = new_otp
                user.save()
                
                print("new otp", new_otp)
                
                return Response({"message":"Otp resend successfully"})
            return Response({"message":"User isn't registered"})
        return Response(serializer.errors)
    

class ForgotPasswordView(APIView):
    
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            
            try:
                user = User.objects.get(email = email)
            
                new_otp = generate_otp()
                user.otp = new_otp
                user.save()
                
                print(f"email:{user.email} new opt:{user.otp}")
                return Response({"message":"new Otp send"})
            
            except User.DoesNotExist:
                return Response({"message":"User doesn't exist"})
        return Response(serializer.errors)
    
class ResetPasswordView(APIView):

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            otp = serializer.validated_data.get('otp')
            password = serializer.validated_data.get('password')
            
            try:
                user = User.objects.get(email=email)
                if user.otp == otp:
                    user.set_password(password)
                    user.otp = None
                    user.save()
                    print(f"email:{user.email} and otp:{user.otp}")
                    return Response({"message":"Password successfully changed"})
            except User.DoesNotExist:
                return Response({"message":"User doesn't found"})
        return Response(serializer.errors)
                
