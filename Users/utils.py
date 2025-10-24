import random
from django.conf import settings
from django.core.mail import send_mail

def generate_otp():
    return str(random.randint(100000, 999999))

def send_verification_mail(user, code):
    main_subject = "Your account verification code"
    message = f"Hi, { user.username }You verification code is {code}"
    
    
    email = send_mail(
        main_subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False
        
    )
    
    return email