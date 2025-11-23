from rest_framework import serializers
from .models import (
    User,
    UserProfile
)
from .utils import generate_otp , send_verification_mail

""" ********************* User serializer **************************** """
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



""" ********************* User registration serializer **************************** """
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields =['email','username', 'password']
        
    def create(self, validate_data):
        user = User.objects.create_user(
            email = validate_data.get('email'),
            username = validate_data.get('username'),
            password = validate_data.get('password')
        )
            
        try:
            verification_otp = generate_otp()
            print("OTP:", verification_otp)
            user.otp = verification_otp
            user.save()
        except AttributeError:
            raise ValueError(
                {"detail":"otp not found"}
            )
            
        print(f"OTP for {user.email}: {user.otp}")

        return user

class VerifyOptSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField();
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
    password = serializers.CharField()
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields ="__all__"