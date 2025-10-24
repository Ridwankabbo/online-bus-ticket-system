from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    
    # To create a custom normal user
    
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Email must be neeaded")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    # For creating a custom Super user
    
    def create_superuser(self, email, username, passwrod=None, **extra_fields):
        
        user  = self.create_user(email, username, passwrod)
        user.is_active = True
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user
    
    
class Users(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email address", max_length=50, unique=True)
    is_active = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username']
    
    def __str__(self):
        return f"{self.username}"
    


