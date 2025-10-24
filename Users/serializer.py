from rest_framework import serializers
from .models import Users
from .utils import generate_otp

class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = '__all__'
        
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
        
    
    def create(self, validated_data):
        user = Users.objects.create_user(
            username=validated_data.get('username'),
            email = validated_data.get('email'),
            password = validated_data.get('password')
        )
        try:
            verification_code = generate_otp()
            user.otp = verification_code
            user.save()
        except user.DoesNotExist:
            raise serializers.ValidationError({
                'detail':"Users model configuration error. 'otp' field not found"
            })
            
        print(f"Email:{user.email} send OTP :{user.otp}")
        return user
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    
class VerifyUserOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
    
class ResendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
    password = serializers.CharField()
    

    
